from agents import Agent
from pydantic import BaseModel, Field
from typing import List
from gemini_config import gemini_model

class DiseaseUnderstandingReport(BaseModel):
    executive_summary: str = Field(description="High-level summary of disease foundations")
    clinical_profile: str = Field(description="Clinical manifestations and progression")
    genetic_landscape: str = Field(description="Genetic factors and mutations")
    epidemiological_context: str = Field(description="Population-level insights")
    omics_insights: str = Field(description="Genomics, proteomics findings")
    key_biological_factors: List[str] = Field(description="Key biological factors identified")
    markdown_report: str = Field(description="Complete disease understanding report in markdown")

DISEASE_SYNTHESIS_INSTRUCTIONS = """You are a Disease Understanding Synthesis Agent specializing in foundational disease analysis.

You will be provided with research findings from four foundational areas:
1. Clinical research results
2. Genetic research results  
3. Epidemiological research results
4. Omics research results

Your task is to synthesize this foundational information into a comprehensive disease understanding report that:
- Provides a solid foundation of disease knowledge
- Identifies key clinical patterns and genetic factors
- Highlights population-level insights
- Integrates omics findings with clinical observations
- Identifies key biological factors that drive the disease
- Sets the stage for deeper pathophysiological analysis

The report should establish a strong foundational understanding that will inform subsequent pathophysiological and pharmacological analysis.
"""

disease_synthesis_agent = Agent(
    name="Disease Understanding Synthesis Agent",
    instructions=DISEASE_SYNTHESIS_INSTRUCTIONS,
    model=gemini_model,
    output_type=DiseaseUnderstandingReport,
)
