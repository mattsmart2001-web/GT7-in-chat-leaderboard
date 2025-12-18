# Streamerbot Automation Files

This folder contains files for **automatic YouTube chat tracking** using Streamerbot.

## 📁 Files in This Folder

### `ChatTrackerAction.cs`
- **What it is:** C# code for Streamerbot
- **What it does:** Captures YouTube chat messages in real-time
- **Setup:** Copy this code into a Streamerbot action
- **Output:** Creates `chat_data.json` with raw tracking data

### `convert_to_leaderboard.py`
- **What it is:** Python script
- **What it does:** Converts `chat_data.json` to leaderboard format
- **How to run:** `python convert_to_leaderboard.py --watch`
- **Output:** Updates `../data.json` for the leaderboard

### `START_TRACKER.bat`
- **What it is:** Windows batch file
- **What it does:** Starts the Python converter in watch mode
- **How to use:** Double-click to start
- **Note:** Keep this window open while streaming!

### `chat_data.json` (Generated)
- **What it is:** Raw chat tracking data
- **Created by:** Streamerbot C# action
- **Format:** Dictionary of user IDs → chatter data
- **Note:** This file is created automatically when chat starts

## 🚀 Quick Setup

1. **Add C# action to Streamerbot:**
   - Copy code from `ChatTrackerAction.cs`
   - Update the file path to match your setup
   - Link to YouTube Message event

2. **Start the converter:**
   - Double-click `START_TRACKER.bat`
   - Or run: `python convert_to_leaderboard.py --watch`

3. **Stream!**
   - Chat messages are tracked automatically
   - Leaderboard updates every 5-30 seconds

## 📖 Full Documentation

See **[../AUTOMATION_SETUP.md](../AUTOMATION_SETUP.md)** for complete instructions, troubleshooting, and customization options.

## 🔧 Requirements

- Streamerbot (connected to YouTube)
- Python 3.7 or newer
- Windows (for .bat file) or any OS for Python script

## ❓ Questions?

Check the main [AUTOMATION_SETUP.md](../AUTOMATION_SETUP.md) guide!
