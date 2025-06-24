#!/usr/bin/env python3
"""
Model Configuration Switcher for Drug Repurposing Deep Search Agent

This script allows you to easily switch between Llama 3.3 (local) and Gemini (cloud) models.
"""

import os
import sys

def update_gemini_config(use_llama=True):
    """Update gemini_config.py to use either Llama 3.3 or Gemini"""
    
    config_file = "gemini_config.py"
    
    if use_llama:
        default_model_line = "default_model = llama3_3_model"
        print("🦙 Switching to Local Llama 3.3...")
    else:
        default_model_line = "default_model = gemini_model"
        print("🤖 Switching to Cloud Gemini...")
    
    # Read current config
    with open(config_file, 'r') as f:
        lines = f.readlines()
    
    # Update the default model line
    updated_lines = []
    for line in lines:
        if line.strip().startswith("default_model ="):
            updated_lines.append(default_model_line + "\n")
        else:
            updated_lines.append(line)
    
    # Write updated config
    with open(config_file, 'w') as f:
        f.writelines(updated_lines)
    
    model_name = "Llama 3.3 (Local)" if use_llama else "Gemini (Cloud)"
    print(f"✅ Successfully switched to {model_name}")
    print(f"📝 Updated {config_file}")
    
    if use_llama:
        print("\n💡 Make sure Ollama is running and Llama 3.3 model is available:")
        print("   ollama serve")
        print("   ollama pull llama3.3:70b-instruct-q4_0")
    else:
        print("\n💡 Make sure your GOOGLE_API_KEY environment variable is set")

def main():
    if len(sys.argv) != 2:
        print("Usage: python switch_model.py [llama|gemini]")
        print("  llama  - Switch to local Llama 3.3")
        print("  gemini - Switch to cloud Gemini")
        sys.exit(1)
    
    model_choice = sys.argv[1].lower()
    
    if model_choice == "llama":
        update_gemini_config(use_llama=True)
    elif model_choice == "gemini":
        update_gemini_config(use_llama=False)
    else:
        print("❌ Invalid choice. Use 'llama' or 'gemini'")
        sys.exit(1)

if __name__ == "__main__":
    main()
