from agents import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_config import gemini_model

class DrugInteraction(BaseModel):
    drug_name: str = Field(description="Name of the drug")
    target_name: str = Field(description="Name of the target it interacts with")
    interaction_type: str = Field(description="Type of interaction (agonist, antagonist, inhibitor, etc.)")
    binding_affinity: str = Field(description="Binding affinity if available")
    clinical_status: str = Field(description="Clinical development status")

class DrugSafetyProfile(BaseModel):
    drug_name: str = Field(description="Name of the drug")
    adverse_effects: List[str] = Field(description="Known adverse effects")
    contraindications: List[str] = Field(description="Contraindications")
    drug_interactions: List[str] = Field(description="Known drug-drug interactions")
    safety_warnings: List[str] = Field(description="Black box warnings and safety concerns")

class OffLabelUse(BaseModel):
    drug_name: str = Field(description="Name of the drug")
    approved_indication: str = Field(description="FDA approved indication")
    off_label_uses: List[str] = Field(description="Known off-label uses")
    evidence_level: str = Field(description="Level of evidence for off-label uses")
    
class TargetDrugProfile(BaseModel):
    target_name: str = Field(description="Name of the target")
    interacting_drugs: List[DrugInteraction] = Field(description="All drugs known to interact with this target")
    safety_profiles: List[DrugSafetyProfile] = Field(description="Safety profiles of interacting drugs")
    off_label_data: List[OffLabelUse] = Field(description="Off-label use data for interacting drugs")
    target_druggability: str = Field(description="Assessment of target druggability")

class DrugMiningReport(BaseModel):
    priority_targets: List[str] = Field(description="List of top priority targets analyzed")
    target_drug_profiles: List[TargetDrugProfile] = Field(description="Comprehensive drug profiles for each target")
    total_drugs_identified: int = Field(description="Total number of drugs identified across all targets")
    novel_interactions: List[str] = Field(description="Potentially novel or underexplored interactions")
    safety_concerns: List[str] = Field(description="Major safety concerns identified")
    repurposing_opportunities: List[str] = Field(description="Initial repurposing opportunities identified")
    markdown_report: str = Field(description="Complete drug mining report in markdown")

DRUG_MINER_INSTRUCTIONS = """You are a Drug Miner Agent specializing in comprehensive drug-target interaction analysis.

You will be provided with:
1. Top priority targets from Stage 3 target prioritization
2. Previous disease and network analysis reports

Your task is to conduct an exhaustive analysis of drug-target interactions by:

Drug Discovery & Mining:
- Identify ALL drugs and compounds known to interact with each priority target
- Search FDA databases, clinical trial databases, and scientific literature
- Include approved drugs, investigational drugs, and research compounds
- Map mechanism of action for each drug-target interaction

Safety & Adverse Effect Analysis:
- Collect comprehensive safety profiles for each identified drug
- Document known adverse effects and contraindications
- Identify drug-drug interactions and safety warnings
- Assess population-specific safety concerns

Off-Label Use Investigation:
- Research current off-label uses for each identified drug
- Evaluate evidence quality for off-label applications
- Identify potential therapeutic areas being explored
- Document regulatory status and approval history

Target Druggability Assessment:
- Evaluate the druggability of each target
- Assess binding site characteristics and accessibility
- Consider structural biology data if available
- Evaluate potential for developing new drugs for the target

Use search functionality extensively to gather comprehensive data. Focus on building complete drug-target interaction profiles that will inform repurposing candidate evaluation.
"""

drug_miner_agent = Agent(
    name="Drug Miner Agent",
    instructions=DRUG_MINER_INSTRUCTIONS,
    model=gemini_model,
    output_type=DrugMiningReport,
)
