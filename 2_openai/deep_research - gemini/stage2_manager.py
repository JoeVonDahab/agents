from agents import Agent, Runner
from pydantic import BaseModel, Field
from typing import List
from gemini_config import gemini_model
import asyncio

class Stage2ResearchPlan(BaseModel):
    clinical_queries: List[str] = Field(description="Clinical research queries (symptoms, progression)")
    genetic_queries: List[str] = Field(description="Genetic research queries (mutations, risk genes)")
    epidemiological_queries: List[str] = Field(description="Epidemiological queries (prevalence, risk factors)")
    omics_queries: List[str] = Field(description="Omics queries (genomics, proteomics data)")

class PathophysiologyResearchPlan(BaseModel):
    pathophysiological_queries: List[str] = Field(description="Advanced pathophysiological queries based on disease and drug understanding")

STAGE2_MANAGER_INSTRUCTIONS = """You are a Stage 2 Research Manager for drug repurposing research. 
Based on the user's answers to initial questions and preliminary findings, you need to create a comprehensive research plan.

You will be provided with:
1. The original disease query
2. User's answers to clarifying questions
3. Initial research findings

Your task is to generate specific search queries for four foundational research areas:
1. Clinical: symptoms, disease progression, clinical manifestations
2. Genetic: known mutations, risk genes, genetic factors
3. Epidemiological: prevalence, risk factors, demographics
4. Omics: genomics, proteomics, transcriptomics data

Generate 2-3 specific, targeted queries for each area that will provide foundational insights into the disease.
Note: Pathophysiological research will be conducted separately in Phase C after initial understanding is built.
"""

PATHOPHYSIOLOGY_MANAGER_INSTRUCTIONS = """You are a Pathophysiology Research Manager specializing in comprehensive molecular mechanism analysis.

You will be provided with:
1. Disease understanding from Phase A (clinical, genetic, epidemiological, omics data)
2. Pharmacological landscape from Phase B (current drugs, targets, mechanisms)

Your task is to generate specific pathophysiological research queries that integrate both disease and drug knowledge:
- Molecular pathways involved in disease progression
- Cellular mechanisms and dysfunction
- Protein interactions and networks
- Metabolic changes and disruptions
- Tissue and organ-level pathological changes
- How current drugs interact with these pathways
- Pathway crosstalk and compensatory mechanisms
- Potential intervention points for drug repurposing

Generate 3-4 highly specific queries that will reveal comprehensive pathophysiological understanding for drug repurposing opportunities.
"""

stage2_manager = Agent(
    name="Stage 2 Manager",
    instructions=STAGE2_MANAGER_INSTRUCTIONS,
    model=gemini_model,
    output_type=Stage2ResearchPlan,
)

pathophysiology_manager = Agent(
    name="Pathophysiology Manager",
    instructions=PATHOPHYSIOLOGY_MANAGER_INSTRUCTIONS,
    model=gemini_model,
    output_type=PathophysiologyResearchPlan,
)
