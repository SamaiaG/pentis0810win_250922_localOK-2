#!/bin/bash
# Pentis 0.8.1 - Game Launcher Script

echo "=================================================="
echo "        PENTIS 0.8.1 BETA - Game Launcher"
echo "=================================================="
echo

# Check Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo

# Check Pygame is installed
python3 -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Error: Pygame is not installed"
    echo "Install with: pip install pygame"
    exit 1
fi

echo "✓ Pygame is installed"
echo

# Navigate to game directory
cd "$(dirname "$0")/pentis" || exit

# Run the game
echo "🎮 Starting Pentis 0.8.1..."
echo

python3 pentis_081_local.py
