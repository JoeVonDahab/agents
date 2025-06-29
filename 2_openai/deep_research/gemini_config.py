import os
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

# Gemini Configuration (kept for potential future use)
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.environ.get('GOOGLE_API_KEY')

gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)

# Llama 3.3 Configuration (Local)
llama3_3_client = AsyncOpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
llama3_3_model = OpenAIChatCompletionsModel(model="llama3.3:70b-instruct-q4_0", openai_client=llama3_3_client)

# Default model (currently using Llama 3.3)
default_model = llama3_3_model
