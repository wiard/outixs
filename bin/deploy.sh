#!/bin/bash

echo "Starting deployment of Bitoshi-Blockamoto-Game-Engine..."

# Step 1: Navigate to the project directory
cd ~/Bitoshi-Blockamoto-Game-Engine || { echo "Project directory not 
found!"; exit 1; }

# Step 2: Run the environment setup script
echo "Setting up environment..."
bash ./scripts/setup_env.sh || { echo "Environment setup failed!"; exit 1; 
}

# Step 3: Initialize the database
echo "Setting up database..."
python3 ./scripts/setup_database.py || { echo "Database setup failed!"; 
exit 1; }

# Step 4: Sync with GitHub (optional step, uncomment if needed)
# echo "Syncing with GitHub..."
# git add .
# git commit -m "Deploying the game engine"
# git push || { echo "GitHub sync failed!"; exit 1; }

echo "Deployment completed successfully!"

