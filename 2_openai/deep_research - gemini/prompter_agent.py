from agents import Agent
from pydantic import BaseModel, Field
from gemini_config import gemini_model

class SearchPlan(BaseModel):
    search_queries: list[str] = Field(description="Exactly 5 search queries for the disease research", max_length=5)

PROMPT = """You are an expert medical researcher. Your goal is to define exactly five key areas for a preliminary search on a given disease.
The user will provide a disease name. You MUST output exactly 5 search queries that will help with the research.
Here are the 5 areas you should focus on:
1. Current medications on the market for the disease.
2. Mechanism of action (MOA) of these drugs.
3. Drugs currently in development (pipeline) for the disease.
4. Promising biological targets for new drugs.
5. A general overview of the disease, including its causes, symptoms, and prognosis.

Return exactly 5 search queries, one for each area above.
"""

prompter_agent = Agent(
    name="Prompter Agent",
    instructions=PROMPT,
    model=gemini_model,
    output_type=SearchPlan,
)
