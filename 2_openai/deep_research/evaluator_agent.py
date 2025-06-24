from agents import Agent
from pydantic import BaseModel, Field
from gemini_config import gemini_model

class RationaleAndQuestions(BaseModel):
    rationales: list[str] = Field(description="List of 5 rationales for the questions that need to be answered.")
    questions: list[str] = Field(description="List of 5 questions for the user based on the rationales.")

PROMPT = """You are an expert medical researcher. Based on the provided research, your goal is to first determine 5 rationales for asking clarifying questions to the user, and then formulate those 5 questions. The user should not know about the initial search. The questions should be designed to narrow down the subsequent research.

You will be provided with initial research findings.

First, analyze the research to identify gaps, ambiguities, or areas needing prioritization.
Based on this analysis, generate 5 distinct rationales for why specific questions need to be asked.
Then, for each rationale, formulate a clear and concise question for the user.

Output the rationales and the questions.
"""

question_generator_agent = Agent(
    name="Question Generator Agent",
    instructions=PROMPT,
    model=gemini_model,
    output_type=RationaleAndQuestions,
)
