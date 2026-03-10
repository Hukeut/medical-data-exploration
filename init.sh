#!/bin/bash

echo "Creating virtual environment: hdenv"
python3 -m venv hdenv

echo "Activating environment"
source hdenv/bin/activate

echo "Upgrading pip"
pip install --upgrade pip

echo "Installing requirements"
pip install -r requirements.txt

echo "Adding Jupyter kernel"
python -m ipykernel install --user --name=hdenv --display-name "Python (hdenv)"

echo "Setup complete!"
echo "Activate the environment with:"
echo "source hdenv/bin/activate"

chmod +x init.sh