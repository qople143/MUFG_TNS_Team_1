#!/bin/bash

# Excel Data Massaging Tool - Setup and Run Script
# This script sets up the environment and runs the application

echo "=================================================="
echo "Excel Data Massaging Tool - Setup & Run"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt -q

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Run tests
echo "🧪 Running tests..."
python3 test_app.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "🚀 Starting Streamlit Application..."
    echo "=================================================="
    echo ""
    echo "The application will open in your browser at:"
    echo "http://localhost:8501"
    echo ""
    echo "Press Ctrl+C to stop the application"
    echo ""
    
    # Run Streamlit
    streamlit run app.py
else
    echo ""
    echo "❌ Tests failed. Please fix the issues before running the application."
    exit 1
fi
