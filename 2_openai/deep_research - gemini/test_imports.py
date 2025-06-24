#!/usr/bin/env python3
"""
Simple test script to verify that all imports work correctly
"""

def test_imports():
    try:
        print("Testing basic imports...")
        import gradio as gr
        print("✅ Gradio imported successfully")
        
        from dotenv import load_dotenv
        print("✅ dotenv imported successfully")
        
        print("\nTesting agent imports...")
        from gemini_config import gemini_model
        print("✅ Gemini config imported successfully")
        
        from research_manager import ResearchManager
        print("✅ Research manager imported successfully")
        
        print("\nTesting Stage 1 agents...")
        from search_agent import search_agent
        from prompter_agent import prompter_agent
        from evaluator_agent import question_generator_agent
        from reporter_agent import reporter_agent
        print("✅ Stage 1 agents imported successfully")
        
        print("\nTesting Stage 2 agents...")
        from stage2_manager import stage2_manager, pathophysiology_manager
        from disease_synthesis_agent import disease_synthesis_agent
        from pharmacology_agent import pharmacology_agent
        from comprehensive_pathophysiology_agent import comprehensive_pathophysiology_agent
        from specialized_research_agents import (
            clinical_research_agent, genetic_research_agent, 
            epidemiological_research_agent, pathophysiological_research_agent, 
            omics_research_agent
        )
        print("✅ Stage 2 agents imported successfully")
        
        print("\nTesting Stage 3 agents...")
        from qsb_modeling_agent import qsb_modeling_agent
        from target_analysis_agent import target_analysis_agent
        from prioritization_agent import prioritization_agent
        print("✅ Stage 3 agents imported successfully")
        
        print("\nTesting main application...")
        import deep_research
        print("✅ Main application imported successfully")
        
        print("\n🎉 All imports successful! The application should work correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    if success:
        print("\n✅ System is ready to run!")
        print("You can now run: python deep_research.py")
    else:
        print("\n❌ System has import issues that need to be resolved.")
