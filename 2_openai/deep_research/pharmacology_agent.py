from agents import Agent
from pydantic import BaseModel, Field
from gemini_config import gemini_model

class PharmacologyReport(BaseModel):
    current_therapies: str = Field(description="Currently approved drugs and treatments")
    pipeline_drugs: str = Field(description="Drugs in development/clinical trials")
    target_mechanisms: str = Field(description="Mechanisms of action for existing drugs")
    drug_repurposing_opportunities: list[str] = Field(description="Potential repurposing candidates")
    pharmacological_gaps: list[str] = Field(description="Unmet therapeutic needs")
    markdown_report: str = Field(description="Complete pharmacology report in markdown")

PHARMACOLOGY_INSTRUCTIONS = """You are a Pharmacology Agent specializing in drug research and repurposing analysis.

You will be provided with:
1. Identified therapeutic targets from disease analysis
2. Current disease understanding
3. User context and priorities

Your task is to conduct comprehensive pharmacological research covering:
- All currently approved drugs for the disease
- Drugs in clinical development (pipeline)
- Mechanisms of action for existing therapies
- Off-target effects that could be leveraged
- Drugs approved for other conditions that target the same pathways
- Identification of drug repurposing opportunities
- Gaps in current therapeutic approaches

Focus on actionable insights for drug repurposing, highlighting existing drugs that could potentially be repositioned for this indication.
"""

pharmacology_agent = Agent(
    name="Pharmacology Agent", 
    instructions=PHARMACOLOGY_INSTRUCTIONS,
    model=gemini_model,
    output_type=PharmacologyReport,
)
