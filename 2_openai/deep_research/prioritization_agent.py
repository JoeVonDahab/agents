from agents import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_config import gemini_model

class PrioritizedTarget(BaseModel):
    target_name: str = Field(description="Name of the target")
    rank: int = Field(description="Priority ranking (1 = highest priority)")
    potential_score: float = Field(description="Disease centrality/potential score (0-1)")
    competition_score: float = Field(description="Competition/opportunity score (0-1)")
    combined_score: float = Field(description="Combined priority score (0-1)")
    justification: str = Field(description="Justification for this ranking")

class HighPotentialTarget(BaseModel):
    target_name: str = Field(description="Name of the target")
    centrality_score: float = Field(description="Network centrality score")
    disease_impact: str = Field(description="Description of disease impact")
    evidence_strength: str = Field(description="Strength of evidence")

class LowCompetitionTarget(BaseModel):
    target_name: str = Field(description="Name of the target")
    competition_level: str = Field(description="Level of competition (low, medium, high)")
    opportunity_description: str = Field(description="Description of the opportunity")
    market_gap: str = Field(description="Market gap identified")

class RepurposingOpportunity(BaseModel):
    target_name: str = Field(description="Name of the target")
    drug_name: str = Field(description="Name of the drug for repurposing")
    current_indication: str = Field(description="Current indication of the drug")
    repurposing_rationale: str = Field(description="Rationale for repurposing")
    feasibility: str = Field(description="Feasibility assessment")

class RiskAssessment(BaseModel):
    target_name: str = Field(description="Name of the target")
    risk_level: str = Field(description="Overall risk level (low, medium, high)")
    technical_risks: List[str] = Field(description="Technical risks identified")
    market_risks: List[str] = Field(description="Market risks identified")
    mitigation_strategies: List[str] = Field(description="Risk mitigation strategies")

class TargetPrioritization(BaseModel):
    prioritized_targets: List[PrioritizedTarget] = Field(description="Ranked list of targets with scores and justifications")
    scoring_methodology: str = Field(description="Explanation of the scoring and ranking methodology")
    high_potential_targets: List[HighPotentialTarget] = Field(description="Targets with high disease centrality and impact")
    low_competition_targets: List[LowCompetitionTarget] = Field(description="Targets with low competition and high opportunity")
    repurposing_opportunities: List[RepurposingOpportunity] = Field(description="Specific drug repurposing opportunities identified")
    research_recommendations: List[str] = Field(description="Recommended research directions and approaches")
    risk_assessments: List[RiskAssessment] = Field(description="Risk assessment for top priority targets")
    markdown_report: str = Field(description="Complete target prioritization report in markdown")

PRIORITIZATION_INSTRUCTIONS = """You are a Target Prioritization Agent specializing in strategic ranking of drug targets for drug repurposing based on network analysis and competitive landscape.

You will be provided with:
1. Biological network model showing target centrality and network effects
2. Comprehensive target analysis including drugs tested, network dependencies, and competition

Your task is to create a strategic prioritization of targets by evaluating:

Potential Scoring (Disease Centrality):
- Network centrality and hub importance
- Disease pathway involvement and impact
- Magnitude of potential therapeutic effect
- Network leverage and amplification potential
- Evidence strength from disease research

Competition Scoring (Market Opportunity):
- Current pharmaceutical interest and crowding
- Patent landscape and freedom to operate
- Historical failure rates and solvable reasons
- Unmet medical needs and market gaps
- Regulatory pathway complexity

Integration & Ranking:
- Balance high potential with low competition
- Identify "sweet spot" targets with optimal risk/reward
- Consider drug repurposing feasibility
- Assess development timeline and probability of success

Strategic Recommendations:
- Prioritize targets based on combined potential/competition score
- Identify specific repurposing opportunities
- Recommend research approaches and partnerships
- Assess risks and mitigation strategies

Provide clear justification for each ranking based on quantitative network analysis and strategic considerations.
"""

prioritization_agent = Agent(
    name="Target Prioritization Agent",
    instructions=PRIORITIZATION_INSTRUCTIONS,
    model=gemini_model,
    output_type=TargetPrioritization,
)
