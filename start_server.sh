#!/bin/bash
# ================================================================
# Start Local Web Server for Leaderboard
# ================================================================
# This starts a local web server so the leaderboard can load data.json
# Keep this terminal open while viewing the leaderboard!
# ================================================================

echo "================================================================"
echo "Starting Leaderboard Server..."
echo "================================================================"
echo ""

# Make sure we're in the script directory
cd "$(dirname "$0")"

# Run the Python server
if command -v python3 &> /dev/null; then
    python3 start_server.py
elif command -v python &> /dev/null; then
    python start_server.py
else
    echo "ERROR: Python is not installed"
    echo ""
    echo "Please install Python 3:"
    echo "  - macOS: brew install python3"
    echo "  - Linux: sudo apt install python3"
    echo ""
    exit 1
fi
