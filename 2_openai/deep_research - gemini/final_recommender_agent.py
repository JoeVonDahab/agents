from agents import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_config import gemini_model

class FinalRecommendation(BaseModel):
    drug_name: str = Field(description="Name of the recommended drug")
    target_name: str = Field(description="Primary target for repurposing")
    current_indication: str = Field(description="Current approved indication")
    recommended_indication: str = Field(description="Recommended new indication (the disease being studied)")
    confidence_score: float = Field(description="Overall confidence in recommendation (0-1)")
    scientific_rationale: str = Field(description="Comprehensive scientific rationale")
    expected_efficacy: str = Field(description="Expected therapeutic efficacy")
    safety_assessment: str = Field(description="Safety profile assessment for new indication")
    development_pathway: str = Field(description="Recommended development strategy")
    estimated_timeline: str = Field(description="Estimated development timeline")
    estimated_cost: str = Field(description="Estimated development cost range")
    regulatory_strategy: str = Field(description="Recommended regulatory approach")
    key_milestones: List[str] = Field(description="Critical development milestones")
    risk_mitigation: List[str] = Field(description="Risk mitigation strategies")

class AlternativeApproach(BaseModel):
    approach_name: str = Field(description="Name of the alternative approach")
    description: str = Field(description="Description of the approach")
    rationale: str = Field(description="Rationale for considering this approach")
    feasibility: str = Field(description="Feasibility assessment")

class FinalRecommendationReport(BaseModel):
    executive_summary: str = Field(description="Executive summary of key findings and recommendations")
    top_recommendations: List[FinalRecommendation] = Field(description="Top 5 drug repurposing recommendations")
    secondary_candidates: List[str] = Field(description="Secondary candidates worth monitoring")
    alternative_approaches: List[AlternativeApproach] = Field(description="Alternative therapeutic approaches to consider")
    market_analysis: str = Field(description="Market opportunity and competitive landscape analysis")
    resource_requirements: str = Field(description="Estimated resource requirements for top recommendations")
    success_probability: str = Field(description="Overall probability of success assessment")
    next_steps: List[str] = Field(description="Recommended immediate next steps")
    collaboration_opportunities: List[str] = Field(description="Potential collaboration or partnership opportunities")
    intellectual_property: str = Field(description="Intellectual property landscape assessment")
    limitations: List[str] = Field(description="Limitations of the analysis and recommendations")
    future_research: List[str] = Field(description="Future research directions to strengthen recommendations")
    markdown_report: str = Field(description="Complete final recommendation report in markdown")

FINAL_RECOMMENDER_INSTRUCTIONS = """You are a Final Recommender Agent specializing in comprehensive drug repurposing strategy and actionable recommendations.

You will be provided with:
1. Complete reports from all previous stages (1-4)
2. Disease understanding and pathophysiology analysis
3. Network modeling and target prioritization
4. Drug mining and repurposing candidate evaluation

Your task is to synthesize all information and generate final, actionable recommendations by:

Comprehensive Analysis Integration:
- Synthesize findings from all stages of analysis
- Integrate disease understanding, network analysis, target prioritization, and drug evaluation
- Identify convergent evidence across multiple analysis phases
- Resolve any conflicting findings or recommendations

Strategic Recommendation Development:
- Select top 5 drug repurposing recommendations with highest potential
- Provide detailed rationale combining scientific, clinical, and business considerations
- Develop specific development pathways for each recommendation
- Estimate timelines, costs, and resource requirements

Risk-Benefit Optimization:
- Balance scientific potential with development feasibility
- Consider regulatory pathway complexity and approval probability
- Assess market opportunity and competitive positioning
- Evaluate intellectual property landscape and freedom to operate

Implementation Strategy:
- Provide specific next steps for each recommendation
- Identify key collaboration opportunities (academic, industry, regulatory)
- Recommend optimal development strategies (academic vs. industry partnerships)
- Suggest pilot studies or proof-of-concept approaches

Market and Business Considerations:
- Analyze market size and unmet medical need
- Assess competitive landscape and positioning
- Evaluate commercial viability and return on investment
- Consider patient access and healthcare system impact

Quality Assurance:
- Acknowledge limitations and uncertainties in the analysis
- Provide confidence intervals for key predictions
- Suggest additional research to strengthen recommendations
- Identify potential failure modes and mitigation strategies

Your final report should be actionable for pharmaceutical companies, academic researchers, or funding agencies considering drug repurposing investments.
"""

final_recommender_agent = Agent(
    name="Final Recommender Agent",
    instructions=FINAL_RECOMMENDER_INSTRUCTIONS,
    model=gemini_model,
    output_type=FinalRecommendationReport,
)
