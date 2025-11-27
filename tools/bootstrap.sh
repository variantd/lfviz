#!/bin/bash
# This script sets up the local development environment.

# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install all required dependencies
pip install fastapi uvicorn plotly dash numpy requests
