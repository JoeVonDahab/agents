from agents import Agent
from gemini_config import gemini_model

PROMPT = """You are a medical reporter. Your goal is to present five questions to the user to help guide further research.
The user will provide a list of questions. You should format them for the user, explaining that their answers will help focus the research.
"""

reporter_agent = Agent(
    name="Reporter Agent",
    instructions=PROMPT,
    model=gemini_model,
)
