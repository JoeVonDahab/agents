from agents import Agent
from pydantic import BaseModel, Field
from gemini_config import gemini_model

class ComprehensivePathophysiologyReport(BaseModel):
    molecular_pathways: str = Field(description="Detailed molecular pathways involved in disease")
    cellular_mechanisms: str = Field(description="Cellular dysfunction and mechanisms")
    protein_networks: str = Field(description="Protein interactions and regulatory networks")
    metabolic_disruptions: str = Field(description="Metabolic changes and disruptions")
    tissue_pathology: str = Field(description="Tissue and organ-level pathological changes")
    drug_pathway_interactions: str = Field(description="How current drugs interact with disease pathways")
    repurposing_targets: list[str] = Field(description="Identified targets for drug repurposing")
    intervention_points: list[str] = Field(description="Potential intervention points in pathways")
    markdown_report: str = Field(description="Complete comprehensive pathophysiology report in markdown")

COMPREHENSIVE_PATHOPHYSIOLOGY_INSTRUCTIONS = """You are a Comprehensive Pathophysiology Agent specializing in integrative molecular mechanism analysis for drug repurposing.

You will be provided with:
1. Disease understanding data (clinical, genetic, epidemiological, omics findings)
2. Pharmacological landscape (current drugs, targets, mechanisms of action)

Your task is to conduct comprehensive pathophysiological analysis that integrates both disease biology and drug mechanisms:

Focus Areas:
- Detailed molecular pathways driving disease progression
- Cellular mechanisms and dysfunction patterns
- Protein interaction networks and regulatory cascades
- Metabolic pathway disruptions and compensatory mechanisms
- Tissue and organ-level pathological changes
- How existing drugs interact with disease pathways
- Pathway crosstalk and network effects
- Identification of novel intervention points
- Potential targets for drug repurposing based on pathway analysis

Provide deep mechanistic insights that bridge disease biology with therapeutic opportunities, highlighting specific molecular targets and pathways that could be leveraged for drug repurposing.
"""

comprehensive_pathophysiology_agent = Agent(
    name="Comprehensive Pathophysiology Agent",
    instructions=COMPREHENSIVE_PATHOPHYSIOLOGY_INSTRUCTIONS,
    model=gemini_model,
    output_type=ComprehensivePathophysiologyReport,
)
