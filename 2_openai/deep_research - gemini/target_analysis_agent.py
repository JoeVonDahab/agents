from agents import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_config import gemini_model

class TargetAssessment(BaseModel):
    target_name: str = Field(description="Name of the target")
    drugs_tested: List[str] = Field(description="List of drugs tested against this target")
    clinical_outcomes: str = Field(description="Summary of clinical trial outcomes")
    mechanism_diversity: str = Field(description="Diversity of mechanisms targeting this protein")

class NetworkEffect(BaseModel):
    target_name: str = Field(description="Name of the target")
    downstream_effects: List[str] = Field(description="Downstream network effects")
    upstream_effects: List[str] = Field(description="Upstream network effects")
    network_amplification: str = Field(description="Network amplification potential")

class TargetDependency(BaseModel):
    target_name: str = Field(description="Name of the target")
    dependencies: List[str] = Field(description="Other network components this target depends on")
    independence_score: str = Field(description="How independent this target's effects are")
    combination_potential: str = Field(description="Potential for combination therapies")

class DruggabilityScore(BaseModel):
    target_name: str = Field(description="Name of the target")
    druggability_score: float = Field(description="Druggability score (0-1)")
    reasoning: str = Field(description="Reasoning behind the score")

class CompetitiveLandscape(BaseModel):
    target_name: str = Field(description="Name of the target")
    pharma_interest: str = Field(description="Current pharmaceutical interest level")
    patent_status: str = Field(description="Patent landscape status")
    research_trends: str = Field(description="Research publication trends")
    unmet_needs: str = Field(description="Unmet needs and opportunities")

class TargetAnalysisReport(BaseModel):
    target_assessments: List[TargetAssessment] = Field(description="Detailed assessment for each target including drugs tested, network effects, dependencies")
    network_effects: List[NetworkEffect] = Field(description="How each target affects the broader disease network")
    target_dependencies: List[TargetDependency] = Field(description="Dependencies and independence of each target's effects")
    druggability_scores: List[DruggabilityScore] = Field(description="Druggability assessment for each target")
    competitive_landscape: List[CompetitiveLandscape] = Field(description="Competition analysis for each target")
    target_gaps: List[str] = Field(description="Identified gaps in target research or drug development")
    markdown_report: str = Field(description="Complete target analysis report in markdown")

TARGET_ANALYSIS_INSTRUCTIONS = """You are a Target Analysis Agent specializing in comprehensive drug target evaluation and competitive landscape analysis.

You will be provided with:
1. Biological network model with identified potential targets
2. Previous disease and pharmacological research

Your task is to conduct deep analysis of each potential target by investigating:

Drug Testing History:
- All drugs that have been tested against each target
- Clinical trial outcomes and failure reasons
- Current drugs in development for each target
- Mechanism of action diversity

Network Effect Analysis:
- How modulating each target affects the broader disease network
- Downstream and upstream effects
- Network propagation and amplification effects
- Potential for network compensation

Target Dependencies:
- How dependent each target's effect is on other network components
- Independent vs. synergistic effects
- Robustness to network perturbations
- Potential for combination therapies

Competitive Assessment:
- Current pharmaceutical interest and investment
- Patent landscape
- Research publication trends
- Unmet needs and opportunities

Use search functionality to fill any missing information gaps. Provide comprehensive analysis that will inform target prioritization.
"""

target_analysis_agent = Agent(
    name="Target Analysis Agent", 
    instructions=TARGET_ANALYSIS_INSTRUCTIONS,
    model=gemini_model,
    output_type=TargetAnalysisReport,
)
