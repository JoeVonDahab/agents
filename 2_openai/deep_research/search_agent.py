from agents import Agent, function_tool
from duckduckgo_search import DDGS
from gemini_config import gemini_model

@function_tool
def web_search(query: str) -> str:
    """
    Performs a web search using DuckDuckGo for the given query and returns the top 5 results.
    Each result is a snippet from the webpage.
    """
    try:
        with DDGS() as ddgs:
            # Using ddgs.text() for raw text results
            results = [r['body'] for r in ddgs.text(query, max_results=5)]
            if not results:
                return "No results found."
            return "\n\n".join(results)
    except Exception as e:
        return f"Search failed: {str(e)}"

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term using the web_search tool and "
    "produce a concise summary of the results. The summary must be 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[web_search],
    model=gemini_model,
)