#!/usr/bin/env python3
"""
Simple deployment/launch script for the Drug Repurposing Deep Search Agent
Handles environment setup and launches the Gradio application.
"""

import os
import sys
from pathlib import Path

def setup_environment():
    """Setup environment variables and paths for deployment"""
    
    # Check for required environment variables
    if not os.getenv('GOOGLE_API_KEY'):
        print("Warning: GOOGLE_API_KEY environment variable not set!")
        print("Please set your Google API key for Gemini models.")
        
    # Add current directory to Python path for local imports
    current_dir = Path(__file__).parent.absolute()
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    
    # If agents library is included locally, add it to path
    agents_path = current_dir / 'agents'
    if agents_path.exists():
        sys.path.insert(0, str(agents_path))
    
    print(f"Working directory: {current_dir}")
    print(f"Python path: {sys.path[:3]}...")  # Show first 3 entries

def main():
    """Main deployment function"""
    print("🚀 Starting Drug Repurposing Deep Search Agent...")
    
    # Setup environment
    setup_environment()
    
    # Import and launch the application
    try:
        from deep_research import ui
        print("✅ Application modules loaded successfully")
        
        # Launch with appropriate settings for different deployment environments
        if os.getenv('HUGGINGFACE_SPACE'):
            # Hugging Face Spaces configuration
            ui.launch(
                server_name="0.0.0.0",
                server_port=7860,
                share=False,
                inbrowser=False
            )
        else:
            # Local development configuration
            ui.launch(
                inbrowser=True,
                share=False
            )
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please ensure all dependencies are installed:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
