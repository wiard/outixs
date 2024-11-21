#!/bin/bash

echo "Setting up environment for Bitoshi-Blockamoto-Game-Engine..."

# Export environment variables
export ENGINE_HOME=~/Bitoshi-Blockamoto-Game-Engine
export PYTHONPATH=$ENGINE_HOME/src:$PYTHONPATH

# Install Python dependencies
echo "Installing dependencies..."
pip3 install -r $ENGINE_HOME/requirements.txt

echo "Environment setup complete!"

