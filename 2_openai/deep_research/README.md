---
title: Drug Repurposing Deep Search Agent
app_file: deep_research.py
sdk: gradio
sdk_version: 5.33.1
---

# Drug Repurposing Deep Search Agent

A multi-stage, agentic drug repurposing research application built with Python, Gradio, and Gemini (Google) models. This system guides users through disease scoping, comprehensive research, and advanced systems biology modeling to produce actionable drug repurposing insights.

## Features

### Stage 1: Initial Disease Scoping & User-Guided Triage
- Disease name validation and guardrails
- Automated search area definition
- Web search using DuckDuckGo for preliminary research
- Intelligent question generation for user guidance
- User input collection with validation

### Stage 2: Comprehensive Research & Synthesis
- **Phase A**: Foundational research across four domains:
  - Clinical research (epidemiology, symptoms, diagnostics)
  - Genetic research (mutations, inheritance, biomarkers)
  - Epidemiological research (prevalence, risk factors)
  - Omics research (genomics, proteomics, metabolomics)
- **Phase B**: Pharmacological landscape analysis
- **Phase C**: Comprehensive pathophysiology integration

### Stage 3: QSB Modeling & Target Prioritization (Automatic)
- **Phase A**: Quantitative Systems Biology (QSB) network construction
- **Phase B**: Target analysis and competitive landscape evaluation  
- **Phase C**: Strategic target prioritization for drug repurposing
- **Note**: Stage 3 runs automatically after Stage 2 completes - no user interaction required

## Architecture

The system uses a modular agent-based architecture with specialized agents for each research phase:

- **Research Manager**: Orchestrates the multi-stage workflow
- **Search Agent**: Performs web searches using DuckDuckGo
- **Specialized Research Agents**: Handle domain-specific research (clinical, genetic, etc.)
- **Synthesis Agents**: Generate comprehensive reports from research findings
- **QSB Modeling Agent**: Constructs biological network models
- **Target Analysis Agent**: Evaluates drug targets and competition
- **Prioritization Agent**: Strategically ranks targets for repurposing

## Requirements

- Python 3.8+
- Google API key for Gemini models
- Custom `agents` library (see deployment notes)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export GOOGLE_API_KEY="your_google_api_key_here"
```

3. **Important**: The `agents` library is a custom dependency not available on PyPI. You'll need to:
   - Include the agents library source code in your project
   - Or install from a private repository
   - Or contact the maintainers for access

## Usage

### Local Development
```bash
python deep_research.py
```

### Gradio Interface
1. **Stage 1 (Optional)**: Enter a disease name to generate targeted research questions
2. **Stage 2 + 3 (Combined)**: Provide detailed disease information (can be answers from Stage 1 or your own comprehensive information)
3. The system will automatically run Stage 2 (comprehensive research) followed by Stage 3 (QSB modeling and target prioritization)
4. Review the complete drug repurposing analysis and target recommendations

## Deployment

### Hugging Face Spaces

This application is designed for deployment on Hugging Face Spaces. Key considerations:

1. **Dependencies**: Ensure all packages in `requirements.txt` are available
2. **Custom Library**: The `agents` library needs to be handled specially:
   - Option 1: Include source code in the repository
   - Option 2: Use pip install from git repository
   - Option 3: Create a wheel package and include it

3. **Environment Variables**: Set up `GOOGLE_API_KEY` in Spaces secrets

4. **Memory**: The application may require higher memory tiers due to the complex multi-agent processing

## API Keys and Configuration

- **GOOGLE_API_KEY**: Required for Gemini model access
- **OpenAI compatibility**: The system uses Gemini through OpenAI-compatible endpoints

## Contributing

This is a research prototype. For production use, consider:
- Adding comprehensive error handling
- Implementing rate limiting for API calls
- Adding user authentication and session management
- Creating data persistence layers
- Adding comprehensive logging and monitoring
