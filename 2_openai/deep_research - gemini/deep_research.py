import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

# Global variable to store the research manager instance
research_manager = None

async def run_stage1(query: str):
    global research_manager
    research_manager = ResearchManager()
    async for chunk in research_manager.run_stage1(query):
        yield chunk

async def run_stage2(user_answers: str):
    global research_manager
    if research_manager is None:
        research_manager = ResearchManager()
    
    # Run Stage 2
    async for chunk in research_manager.run_stage2(user_answers):
        yield chunk
    
    # Automatically run Stage 3 after Stage 2 completes
    yield "\n\n---\n\n# Starting Stage 3: QSB Modeling & Target Prioritization\n"
    yield "Automatically proceeding to Stage 3...\n"
    
    # Check if Stage 2 results are available
    if not hasattr(research_manager, 'last_comprehensive_pathophysiology_report') or \
       not hasattr(research_manager, 'last_disease_report') or \
       not hasattr(research_manager, 'last_pharmacology_report'):
        yield "Error: Stage 2 results are incomplete. Cannot proceed to Stage 3."
        return
    
    async for chunk in research_manager.run_stage3(
        research_manager.last_comprehensive_pathophysiology_report,
        research_manager.last_disease_report,
        research_manager.last_pharmacology_report
    ):
        yield chunk
    
    # Automatically run Stage 4 after Stage 3 completes
    yield "\n\n---\n\n# Starting Stage 4: Drug-Target Deep Dive & Final Recommendations\n"
    yield "Automatically proceeding to Stage 4...\n"
    
    # Check if Stage 3 results are available
    if not hasattr(research_manager, 'last_target_prioritization') or \
       not hasattr(research_manager, 'last_network_model') or \
       not hasattr(research_manager, 'last_target_analysis'):
        yield "Error: Stage 3 results are incomplete. Cannot proceed to Stage 4."
        return
    
    async for chunk in research_manager.run_stage4(
        research_manager.last_target_prioritization,
        research_manager.last_network_model,
        research_manager.last_target_analysis,
        research_manager.last_disease_report,
        research_manager.last_pharmacology_report,
        research_manager.last_comprehensive_pathophysiology_report
    ):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Drug Repurposing Deep Search Agent")
    gr.Markdown("## Multi-Stage Agentic Research System for Drug Repurposing")
    gr.Markdown("Navigate through the stages to build comprehensive drug repurposing insights.")
    
    with gr.Tab("Stage 1: Initial Analysis"):
        gr.Markdown("## Stage 1: Disease Scoping & Question Generation")
        gr.Markdown("Start by providing a disease name to generate targeted research questions.")
        query_textbox = gr.Textbox(label="What disease would you like to research for drug repurposing?", placeholder="e.g., Parkinson's Disease")
        stage1_button = gr.Button("Start Stage 1 Analysis", variant="primary")
        stage1_report = gr.Markdown(label="Stage 1 Results")
        
        stage1_button.click(fn=run_stage1, inputs=query_textbox, outputs=stage1_report)
        query_textbox.submit(fn=run_stage1, inputs=query_textbox, outputs=stage1_report)
    
    with gr.Tab("Stage 2-4: Complete Analysis & Final Recommendations"):
        gr.Markdown("## Stage 2: Comprehensive Research & Synthesis")
        gr.Markdown("## Stage 3: QSB Modeling & Target Prioritization")
        gr.Markdown("## Stage 4: Drug-Target Deep Dive & Final Recommendations")
        gr.Markdown("*Provide detailed answers about the disease to proceed with comprehensive analysis. Stages 2, 3, and 4 will run automatically in sequence.*")
        gr.Markdown("**You can either:**")
        gr.Markdown("- Answer the questions from Stage 1, OR")
        gr.Markdown("- Provide your own detailed information about the disease including clinical presentation, pathways, genetics, etc.")
        
        user_answers_textbox = gr.Textbox(
            label="Your detailed information about the disease", 
            placeholder="Please provide detailed information about the disease including clinical presentation, pathways, known genetics, epidemiology, etc. You can answer the questions from Stage 1 or provide your own comprehensive information...",
            lines=8
        )
        stage2_button = gr.Button("Start Complete Analysis (Stages 2-4)", variant="primary")
        stage2_report = gr.Markdown(label="Complete Analysis Results")
        
        stage2_button.click(fn=run_stage2, inputs=user_answers_textbox, outputs=stage2_report)
    
    # Developer signature at the bottom
    gr.Markdown("""
    <div style="text-align: center; font-size: 13px; color: #666; margin-top: 30px; padding: 10px;">
    <hr>
    <em>
    By: <strong>Youssef Abo-Dahab, Pharm.D</strong><br> 
    M.S Candidate, AI & Computational Drug Discovery<br>
    Zhao Lab, Bioengineering and Therapeutic Sciences Department, UCSF<br>
    youssef.abo-dahab@ucsf.edu
    </em>
    </div>
    """)

ui.launch(inbrowser=True)

