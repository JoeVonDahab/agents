from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from prompter_agent import prompter_agent, SearchPlan
from evaluator_agent import question_generator_agent, RationaleAndQuestions
from reporter_agent import reporter_agent
from stage2_manager import stage2_manager, Stage2ResearchPlan, pathophysiology_manager, PathophysiologyResearchPlan
from disease_synthesis_agent import disease_synthesis_agent, DiseaseUnderstandingReport
from pharmacology_agent import pharmacology_agent, PharmacologyReport
from comprehensive_pathophysiology_agent import comprehensive_pathophysiology_agent, ComprehensivePathophysiologyReport
from qsb_modeling_agent import qsb_modeling_agent, BiologicalNetworkModel
from target_analysis_agent import target_analysis_agent, TargetAnalysisReport
from prioritization_agent import prioritization_agent, TargetPrioritization
from specialized_research_agents import (
    clinical_research_agent, genetic_research_agent, epidemiological_research_agent,
    pathophysiological_research_agent, omics_research_agent
)
import asyncio

class ResearchManager:

    async def run_stage1(self, query: str):
        """ Run Stage 1: Initial Disease Scoping & User-Guided Triage"""
        # Guardrail: Validate disease name input
        if not query or not query.strip():
            yield "Error: Please provide a disease name to research."
            return
            
        # Basic validation for disease name
        query = query.strip()
        if len(query) < 2:
            yield "Error: Please provide a valid disease name (at least 2 characters)."
            return
            
        # Check if input looks like a disease name (basic heuristic)
        if any(char in query.lower() for char in ['?', 'how', 'what', 'why', 'when', 'where']):
            yield "Error: Please provide a disease name only, not a question. Example: 'Parkinson's Disease'"
            return
            
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            yield f"Starting research for disease: {query}"
            
            yield "Defining search areas..."
            search_queries = await self.define_search_areas(query)
            
            yield "Performing preliminary search..."
            search_results = await self.perform_searches(search_queries)
            
            yield "Generating questions for user..."
            rationales_and_questions = await self.generate_questions(search_results)
            
            yield "Presenting questions to user..."
            questions_report = await self.present_questions(rationales_and_questions.questions)
            
            # Store search results for Stage 2
            self.stage1_search_results = search_results
            self.original_query = query
            
            yield questions_report

    async def run_stage2(self, user_answers: str):
        """ Run Stage 2: Comprehensive Research & Synthesis with user answers"""
        # Guardrail: Validate user answers input
        if not user_answers or not user_answers.strip():
            yield "Error: Please provide answers to the questions before proceeding with comprehensive analysis."
            return
            
        user_answers = user_answers.strip()
        if len(user_answers) < 10:
            yield "Error: Please provide more detailed answers to the questions (at least 10 characters)."
            return
            
        # If Stage 1 wasn't run, we need to extract disease name from user answers
        if not hasattr(self, 'original_query'):
            # Try to extract disease name from user answers
            lines = user_answers.split('\n')
            disease_candidates = []
            for line in lines:
                if any(keyword in line.lower() for keyword in ['disease', 'syndrome', 'disorder', 'cancer', 'diabetes', 'parkinson', 'alzheimer']):
                    disease_candidates.append(line.strip())
            
            if disease_candidates:
                # Use the first likely disease mention as the query
                self.original_query = disease_candidates[0]
                # Create minimal search results for Stage 2 planning
                self.stage1_search_results = [f"User provided information about {self.original_query}: {user_answers}"]
            else:
                yield "Error: Could not identify the disease being researched. Please include the disease name in your answers."
                return
            
        yield "Starting comprehensive research phase..."
        stage2_plan = await self.create_stage2_plan(self.original_query, user_answers, self.stage1_search_results)
        
        yield "Phase A: Disease Understanding - Conducting foundational research..."
        disease_research_results = await self.conduct_foundational_research(stage2_plan)
        
        yield "Synthesizing disease understanding report..."
        disease_report = await self.synthesize_disease_understanding(disease_research_results)
        # Store for Stage 3
        self.last_disease_report = disease_report
        
        yield "Phase B: Pharmacology - Analyzing therapeutic landscape..."
        pharmacology_report = await self.analyze_pharmacology(disease_report)
        # Store for Stage 3
        self.last_pharmacology_report = pharmacology_report
        
        yield "Phase C: Comprehensive Pathophysiology - Integrating disease and drug knowledge..."
        pathophysiology_plan = await self.create_pathophysiology_plan(disease_report, pharmacology_report)
        pathophysiology_research = await self.conduct_pathophysiology_research(pathophysiology_plan)
        comprehensive_pathophysiology_report = await self.synthesize_comprehensive_pathophysiology(
            disease_report, pharmacology_report, pathophysiology_research
        )
        # Store for Stage 3
        self.last_comprehensive_pathophysiology_report = comprehensive_pathophysiology_report
        
        yield "Stage 2 complete. Comprehensive analysis ready."
        final_report = f"{disease_report.markdown_report}\n\n---\n\n{pharmacology_report.markdown_report}\n\n---\n\n{comprehensive_pathophysiology_report.markdown_report}"
        yield final_report

    async def run_stage3(self, comprehensive_pathophysiology_report: ComprehensivePathophysiologyReport,
                         disease_report: DiseaseUnderstandingReport, 
                         pharmacology_report: PharmacologyReport):
        """ Run Stage 3: QSB Modeling & Target Prioritization"""
        
        yield "Starting Stage 3: QSB Modeling & Target Prioritization..."
        
        yield "Phase A: Constructing biological network model..."
        network_model = await self.construct_biological_network(
            comprehensive_pathophysiology_report, disease_report, pharmacology_report
        )
        
        yield "Phase B: Analyzing targets and competitive landscape..."
        target_analysis = await self.analyze_targets(network_model)
        
        yield "Phase C: Prioritizing targets based on potential and competition..."
        target_prioritization = await self.prioritize_targets(network_model, target_analysis)
        
        yield "Stage 3 complete. Target prioritization ready."
        final_stage3_report = f"{network_model.markdown_report}\n\n---\n\n{target_analysis.markdown_report}\n\n---\n\n{target_prioritization.markdown_report}"
        yield final_stage3_report

    async def run(self, query: str):
        """ Legacy method for backward compatibility - runs only Stage 1"""
        async for chunk in self.run_stage1(query):
            yield chunk

    # Stage 1 methods (existing)
    async def define_search_areas(self, query: str) -> list[str]:
        """ Define the five key areas for a preliminary search on a given disease """
        result = await Runner.run(
            prompter_agent,
            query,
        )
        search_plan = result.final_output_as(SearchPlan)
        return search_plan.search_queries

    async def perform_searches(self, search_queries: list[str]) -> list[str]:
        """ Perform the searches to perform for the query """
        results = []
        for i, query in enumerate(search_queries):
            result = await self.search(query)
            if result is not None:
                results.append(result)
            print(f"Searching... {i+1}/{len(search_queries)} completed")
        print("Finished searching")
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

    # Stage 2 methods (new)
    async def create_stage2_plan(self, original_query: str, user_answers: str, initial_findings: list[str]) -> Stage2ResearchPlan:
        """ Create a comprehensive research plan for Stage 2 """
        input_data = f"Original Query: {original_query}\nUser Answers: {user_answers}\nInitial Findings: {initial_findings}"
        result = await Runner.run(
            stage2_manager,
            input_data,
        )
        return result.final_output_as(Stage2ResearchPlan)

    async def conduct_foundational_research(self, plan: Stage2ResearchPlan) -> dict:
        """ Conduct foundational research across four areas (excluding pathophysiology) """
        research_tasks = {
            'clinical': self.conduct_research_area(clinical_research_agent, plan.clinical_queries),
            'genetic': self.conduct_research_area(genetic_research_agent, plan.genetic_queries),
            'epidemiological': self.conduct_research_area(epidemiological_research_agent, plan.epidemiological_queries),
            'omics': self.conduct_research_area(omics_research_agent, plan.omics_queries)
        }
        
        results = {}
        for area, task in research_tasks.items():
            results[area] = await task
            print(f"Completed {area} research")
            
        return results

    async def conduct_research_area(self, agent, queries: list[str]) -> list[str]:
        """ Conduct research for a specific area """
        results = []
        for query in queries:
            try:
                result = await Runner.run(agent, query)
                results.append(str(result.final_output))
            except Exception as e:
                print(f"Research failed for query: {query}, error: {e}")
        return results

    async def synthesize_disease_understanding(self, research_results: dict) -> DiseaseUnderstandingReport:
        """ Synthesize foundational research into a disease understanding report """
        input_data = f"Foundational Research Results: {research_results}"
        result = await Runner.run(
            disease_synthesis_agent,
            input_data,
        )
        return result.final_output_as(DiseaseUnderstandingReport)

    async def analyze_pharmacology(self, disease_report: DiseaseUnderstandingReport) -> PharmacologyReport:
        """ Analyze pharmacological landscape based on disease understanding """
        input_data = f"Disease Report: {disease_report.markdown_report}\nKey Biological Factors: {disease_report.key_biological_factors}"
        result = await Runner.run(
            pharmacology_agent,
            input_data,
        )
        return result.final_output_as(PharmacologyReport)

    async def create_pathophysiology_plan(self, disease_report: DiseaseUnderstandingReport, pharmacology_report: PharmacologyReport) -> PathophysiologyResearchPlan:
        """ Create pathophysiology research plan based on disease understanding and pharmacology """
        input_data = f"Disease Understanding: {disease_report.markdown_report}\nPharmacology Report: {pharmacology_report.markdown_report}"
        result = await Runner.run(
            pathophysiology_manager,
            input_data,
        )
        return result.final_output_as(PathophysiologyResearchPlan)

    async def conduct_pathophysiology_research(self, plan: PathophysiologyResearchPlan) -> list[str]:
        """ Conduct comprehensive pathophysiology research """
        results = []
        for query in plan.pathophysiological_queries:
            try:
                result = await Runner.run(pathophysiological_research_agent, query)
                results.append(str(result.final_output))
                print(f"Completed pathophysiology query: {query[:50]}...")
            except Exception as e:
                print(f"Pathophysiology research failed for query: {query}, error: {e}")
        return results

    async def synthesize_comprehensive_pathophysiology(self, disease_report: DiseaseUnderstandingReport, 
                                                     pharmacology_report: PharmacologyReport, 
                                                     pathophysiology_research: list[str]) -> ComprehensivePathophysiologyReport:
        """ Synthesize comprehensive pathophysiology report integrating all knowledge """
        input_data = f"Disease Understanding: {disease_report.markdown_report}\nPharmacology Report: {pharmacology_report.markdown_report}\nPathophysiology Research: {pathophysiology_research}"
        result = await Runner.run(
            comprehensive_pathophysiology_agent,
            input_data,
        )
        return result.final_output_as(ComprehensivePathophysiologyReport)

    # Stage 3 methods
    async def construct_biological_network(self, pathophysiology_report: ComprehensivePathophysiologyReport,
                                         disease_report: DiseaseUnderstandingReport,
                                         pharmacology_report: PharmacologyReport) -> BiologicalNetworkModel:
        """ Construct QSB biological network model from all prior information """
        input_data = f"Pathophysiology: {pathophysiology_report.markdown_report}\nDisease Understanding: {disease_report.markdown_report}\nPharmacology: {pharmacology_report.markdown_report}"
        result = await Runner.run(
            qsb_modeling_agent,
            input_data,
        )
        return result.final_output_as(BiologicalNetworkModel)

    async def analyze_targets(self, network_model: BiologicalNetworkModel) -> TargetAnalysisReport:
        """ Analyze each potential target for drugs tested, network effects, and dependencies """
        input_data = f"Network Model: {network_model.markdown_report}\nPotential Targets: {network_model.potential_targets}"
        
        # Conduct additional searches for each target to fill information gaps
        target_search_results = []
        for target in network_model.potential_targets[:5]:  # Limit to top 5 targets to avoid rate limits
            search_query = f"{target} drug target clinical trials drugs tested mechanism network effects"
            search_result = await self.search(search_query)
            if search_result:
                target_search_results.append(f"Target {target}: {search_result}")
        
        enhanced_input = f"{input_data}\nAdditional Target Research: {target_search_results}"
        result = await Runner.run(
            target_analysis_agent,
            enhanced_input,
        )
        return result.final_output_as(TargetAnalysisReport)

    async def prioritize_targets(self, network_model: BiologicalNetworkModel, 
                               target_analysis: TargetAnalysisReport) -> TargetPrioritization:
        """ Prioritize targets based on potential and competition analysis """
        input_data = f"Network Model: {network_model.markdown_report}\nTarget Analysis: {target_analysis.markdown_report}"
        result = await Runner.run(
            prioritization_agent,
            input_data,
        )
        return result.final_output_as(TargetPrioritization)