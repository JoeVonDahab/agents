#!/bin/bash

# Setup script for Drug Repurposing Deep Search Agent with Local Llama 3.3

echo "🚀 Setting up Drug Repurposing Deep Search Agent with Local Llama 3.3"
echo "=========================================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

echo "✅ pip found"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed successfully"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "🔽 Ollama not found. Installing Ollama..."
    curl -fsSL https://ollama.ai/install.sh | sh
    
    if [ $? -eq 0 ]; then
        echo "✅ Ollama installed successfully"
    else
        echo "❌ Failed to install Ollama"
        exit 1
    fi
else
    echo "✅ Ollama already installed"
fi

# Start Ollama service if not running
if ! pgrep -x "ollama" > /dev/null; then
    echo "🚀 Starting Ollama service..."
    ollama serve &
    sleep 5
    echo "✅ Ollama service started"
else
    echo "✅ Ollama service already running"
fi

# Pull Llama 3.3 model
echo "📥 Pulling Llama 3.3 model (this may take a while - ~40GB download)..."
ollama pull llama3.3:70b-instruct-q4_0

if [ $? -eq 0 ]; then
    echo "✅ Llama 3.3 model pulled successfully"
else
    echo "❌ Failed to pull Llama 3.3 model"
    echo "💡 You can try manually: ollama pull llama3.3:70b-instruct-q4_0"
fi

# Test the setup
echo "🧪 Testing the setup..."
python3 test_imports.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "🚀 To start the application, run:"
    echo "   python3 deep_research.py"
    echo ""
    echo "💡 The application will be available at: http://localhost:7860"
    echo ""
    echo "📋 System Requirements:"
    echo "   - RAM: 16GB+ recommended for Llama 3.3 70B"
    echo "   - Storage: ~40GB for the model"
    echo "   - CPU: Multi-core processor recommended"
    echo ""
    echo "🔧 Troubleshooting:"
    echo "   - If Ollama fails to start: sudo systemctl start ollama"
    echo "   - If model download fails: Check internet connection and disk space"
    echo "   - If application is slow: Consider using smaller model (llama3.1:8b)"
    echo ""
else
    echo "❌ Setup test failed. Please check the error messages above."
fi
