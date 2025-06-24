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
        yield "Error: Please run Stage 1 first"
        return
    
    async for chunk in research_manager.run_stage2(user_answers):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Drug Repurposing Deep Search Agent")
    
    with gr.Tab("Stage 1: Initial Analysis"):
        gr.Markdown("## Stage 1: Disease Scoping & Question Generation")
        query_textbox = gr.Textbox(label="What disease would you like to research for drug repurposing?", placeholder="e.g., Parkinson's Disease")
        stage1_button = gr.Button("Start Stage 1 Analysis", variant="primary")
        stage1_report = gr.Markdown(label="Stage 1 Results")
        
        stage1_button.click(fn=run_stage1, inputs=query_textbox, outputs=stage1_report)
        query_textbox.submit(fn=run_stage1, inputs=query_textbox, outputs=stage1_report)
    
    with gr.Tab("Stage 2: Comprehensive Analysis"):
        gr.Markdown("## Stage 2: Answer Questions & Get Comprehensive Report")
        gr.Markdown("*Complete Stage 1 first, then answer the questions below to proceed with comprehensive analysis.*")
        
        user_answers_textbox = gr.Textbox(
            label="Your answers to the questions from Stage 1", 
            placeholder="Please provide detailed answers to the questions presented in Stage 1...",
            lines=5
        )
        stage2_button = gr.Button("Start Stage 2 Analysis", variant="primary")
        stage2_report = gr.Markdown(label="Stage 2 Results")
        
        stage2_button.click(fn=run_stage2, inputs=user_answers_textbox, outputs=stage2_report)

ui.launch(inbrowser=True)

