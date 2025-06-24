from pydantic import BaseModel, Field
from agents import Agent
from gemini_config import gemini_model

INSTRUCTIONS = (
    "You are a senior researcher tasked with writing a cohesive 'Initial Background Report' for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should compile the findings into a report."
    "The final output should be in markdown format."
)


class InitialBackgroundReportData(BaseModel):
    markdown_report: str = Field(description="The initial background report")


writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model=gemini_model,
    output_type=InitialBackgroundReportData,
)