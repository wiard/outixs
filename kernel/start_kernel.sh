#!/bin/bash

# Start the Bitoshi Blockamoto Kernel
echo "Starting Bitoshi Blockamoto Kernel..."

# Load kernel configuration
CONFIG_FILE="./kernel_config.json"
if [ -f "$CONFIG_FILE" ]; then
  echo "Loading configuration from $CONFIG_FILE..."
else
  echo "Configuration file not found! Exiting..."
  exit 1
fi

# Start peer-to-peer synchronization
echo "Initializing peer-to-peer synchronization..."
python3 ../src/peer_network.py --config "$CONFIG_FILE"

# Confirm kernel startup
echo "Bitoshi Blockamoto Kernel started successfully."

