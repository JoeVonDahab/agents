from agents import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_config import gemini_model

class RepurposingCandidate(BaseModel):
    drug_name: str = Field(description="Name of the candidate drug")
    target_name: str = Field(description="Target the drug interacts with")
    current_indication: str = Field(description="Current approved indication")
    repurposing_score: float = Field(description="Repurposing potential score (0-1)")
    safety_score: float = Field(description="Safety profile score (0-1)")
    efficacy_potential: str = Field(description="Predicted efficacy for the new indication")
    development_feasibility: str = Field(description="Feasibility of repurposing development")
    rationale: str = Field(description="Scientific rationale for repurposing")
    
class TargetEvaluation(BaseModel):
    target_name: str = Field(description="Name of the target")
    priority_rank: int = Field(description="Priority ranking from Stage 3")
    candidate_drugs: List[RepurposingCandidate] = Field(description="Ranked candidate drugs for this target")
    target_assessment: str = Field(description="Overall assessment of repurposing potential for this target")
    risk_factors: List[str] = Field(description="Risk factors for repurposing approaches")
    opportunities: List[str] = Field(description="Key opportunities identified")

class RepurposingEvaluationReport(BaseModel):
    target_evaluations: List[TargetEvaluation] = Field(description="Evaluation for each priority target")
    top_candidates: List[RepurposingCandidate] = Field(description="Top repurposing candidates across all targets")
    evaluation_methodology: str = Field(description="Methodology used for candidate evaluation and scoring")
    success_factors: List[str] = Field(description="Key factors that determine repurposing success")
    development_timeline: str = Field(description="Estimated development timeline for top candidates")
    regulatory_considerations: List[str] = Field(description="Regulatory pathway considerations")
    markdown_report: str = Field(description="Complete repurposing evaluation report in markdown")

REPURPOSING_EVALUATOR_INSTRUCTIONS = """You are a Repurposing Evaluator Agent specializing in drug repurposing candidate assessment and ranking.

You will be provided with:
1. Drug mining report with comprehensive drug-target interaction data
2. Target prioritization results from Stage 3
3. All previous disease and network analysis

Your task is to evaluate and rank drug repurposing candidates by:

Candidate Drug Evaluation:
- Analyze each drug's repurposing potential for the target disease
- Score candidates based on mechanism alignment with disease pathology
- Evaluate existing safety data and adverse effect profiles
- Assess clinical trial feasibility and regulatory pathway

Multi-Criteria Scoring:
- Repurposing Score: Mechanism fit, target relevance, disease pathway alignment
- Safety Score: Known adverse effects, contraindications, drug interactions
- Efficacy Potential: Predicted therapeutic effect based on mechanism
- Development Feasibility: Time, cost, regulatory complexity

Target-Specific Analysis:
- Rank candidates for each priority target
- Consider target-specific factors (druggability, binding sites)
- Evaluate combination therapy potential
- Assess competitive landscape for each target

Cross-Target Prioritization:
- Identify drugs that target multiple priority targets
- Rank candidates across all targets globally
- Consider polypharmacology benefits and risks
- Prioritize based on overall repurposing potential

Risk-Benefit Assessment:
- Evaluate development risks vs. potential benefits
- Consider market factors and unmet medical needs
- Assess probability of clinical success
- Identify key success factors and failure modes

Provide comprehensive candidate rankings with clear justification for each scoring decision.
"""

repurposing_evaluator_agent = Agent(
    name="Repurposing Evaluator Agent",
    instructions=REPURPOSING_EVALUATOR_INSTRUCTIONS,
    model=gemini_model,
    output_type=RepurposingEvaluationReport,
)
