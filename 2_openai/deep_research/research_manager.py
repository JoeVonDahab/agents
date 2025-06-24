from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from prompter_agent import prompter_agent
from evaluator_agent import question_generator_agent, RationaleAndQuestions
from reporter_agent import reporter_agent
import asyncio

class ResearchManager:

    async def run(self, query: str):
        """ Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            
            yield "Defining search areas..."
            search_queries = await self.define_search_areas(query)
            
            yield "Performing preliminary search..."
            search_results = await self.perform_searches(search_queries)
            
            yield "Generating questions for user..."
            rationales_and_questions = await self.generate_questions(search_results)
            
            yield "Presenting questions to user..."
            report = await self.present_questions(rationales_and_questions.questions)

            yield report

    async def define_search_areas(self, query: str) -> list[str]:
        """ Define the five key areas for a preliminary search on a given disease """
        result = await Runner.run(
            prompter_agent,
            query,
        )
        return result.final_output

    async def perform_searches(self, search_queries: list[str]) -> list[str]:
        """ Perform the searches to perform for the query """
        tasks = [asyncio.create_task(self.search(query)) for query in search_queries]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
        return results

    async def search(self, query: str) -> str | None:
        """ Perform a search for the query """
        try:
            result = await Runner.run(
                search_agent,
                query,
            )
            return str(result.final_output)
        except Exception:
            return None

    async def generate_questions(self, search_results: list[str]) -> RationaleAndQuestions:
        """ Generate rationales and questions based on search results """
        result = await Runner.run(
            question_generator_agent,
            str(search_results),
        )
        return result.final_output_as(RationaleAndQuestions)

    async def present_questions(self, questions: list[str]) -> str:
        """ Present questions to the user """
        result = await Runner.run(
            reporter_agent,
            str(questions),
        )
        return result.final_output