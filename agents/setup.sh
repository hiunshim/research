#!/bin/bash

# Create a virtual environment if it doesn't already exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Dependencies installed from requirements.txt."
else
    echo "requirements.txt not found."
fi

# Inform the user about activation and deactivation
echo "To activate the virtual environment, run: source .venv/bin/activate"
echo "To deactivate, simply run: deactivate"

