---
title: Drug Repurposing Deep Search Agent
app_file: deep_research.py
sdk: gradio
sdk_version: 5.33.1
---

# Drug Repurposing Deep Search Agent

A multi-stage, agentic drug repurposing research application built with Python, Gradio, and Llama 3.3 (local). This system guides users through disease scoping, comprehensive research, and advanced systems biology modeling to produce actionable drug repurposing insights.

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

### Stage 4: Drug-Target Deep Dive & Final Recommendations (Automatic)
- **Phase A**: Exhaustive drug mining for priority targets
- **Phase B**: Repurposing candidate evaluation and ranking
- **Phase C**: Final actionable recommendations with development pathways

## Requirements

- Python 3.8+
- **Ollama with Llama 3.3**: Local LLM deployment
- Custom `agents` library (see deployment notes)

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Local Llama 3.3
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull Llama 3.3 model (70B quantized)
ollama pull llama3.3:70b-instruct-q4_0

# Start Ollama server (if not already running)
ollama serve
```

### 3. Custom Agents Library
The `agents` library is a custom dependency not available on PyPI. You'll need to:
- Include the agents library source code in your project
- Or install from a private repository
- Or contact the maintainers for access

## Usage

### Gradio Interface
1. **Stage 1 (Optional)**: Enter a disease name to generate targeted research questions
2. **Stage 2-4 (Combined)**: Provide detailed disease information (can be answers from Stage 1 or your own comprehensive information)
3. The system will automatically run Stage 2 (comprehensive research) → Stage 3 (QSB modeling) → Stage 4 (final recommendations)
4. Review the complete drug repurposing analysis and actionable recommendations

## API Configuration

The system supports both local and cloud-based LLMs:

### Current Configuration (Local Llama 3.3)
```python
llama3_3_client = AsyncOpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
llama3_3_model = OpenAIChatCompletionsModel(model="llama3.3:70b-instruct-q4_0", openai_client=llama3_3_client)
```

### Alternative Configuration (Gemini - Available)
```python
# Gemini configuration is maintained for potential future use
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)
```

## Performance Considerations

- **Local LLM**: Requires significant computational resources (16GB+ RAM recommended for 70B model)
- **Model Size**: Using quantized 4-bit version for balance of performance and resource usage
- **Processing Time**: Local models may be slower than cloud APIs but provide complete privacy and control

## Deployment

### Local Development
```bash
python deep_research.py
```

### Production Deployment
For production deployment, consider:
- Cloud deployment with GPU instances for better performance
- Model serving optimizations (vLLM, TensorRT)
- Load balancing for concurrent users
- Caching mechanisms for repeated queries

## Developer

**Developed by:**  
Youssef Abo-Dahab, Pharm.D  
M.S Candidate, Artificial Intelligence and Computational Drug Discovery and Development  
Zhao Lab, Bioengineering and Therapeutic Sciences Department  
University of California, San Francisco  
📧 youssef.abo-dahab@ucsf.edu

## Contributing

This is a research prototype. For production use, consider:
- Adding comprehensive error handling
- Implementing rate limiting for API calls
- Adding user authentication and session management
- Creating data persistence layers
- Adding comprehensive logging and monitoring
