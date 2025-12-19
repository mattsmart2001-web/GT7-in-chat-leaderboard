#!/usr/bin/env python3
"""
YouTube Chat to Leaderboard Converter
======================================
Converts Streamerbot chat data to leaderboard format.

This script reads the chat_data.json created by Streamerbot
and converts it to the data.json format used by the leaderboard.

Usage:
    python convert_to_leaderboard.py

Options:
    --watch : Continuously watch for changes and auto-update (recommended)
    --once  : Run once and exit
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
CHAT_DATA_FILE = SCRIPT_DIR / "chat_data.json"
LEADERBOARD_DATA_FILE = SCRIPT_DIR.parent / "data.json"
WATCH_INTERVAL = 5  # seconds between checks in watch mode

def generate_avatar_url(username):
    """Generate avatar URL using ui-avatars.com API"""
    colors = [
        '6366f1', '8b5cf6', 'ec4899', '10b981', 'f59e0b',
        '3b82f6', 'ef4444', '14b8a6', 'a855f7', '06b6d4'
    ]
    # Use hash of username to consistently assign same color
    color_index = hash(username) % len(colors)
    color = colors[color_index]
    return f"https://ui-avatars.com/api/?name={username}&background={color}&color=fff&size=100"

def convert_chat_data():
    """Convert chat_data.json to leaderboard data.json format"""
    try:
        # Check if chat data exists
        if not CHAT_DATA_FILE.exists():
            print(f"⚠️  Chat data file not found: {CHAT_DATA_FILE}")
            print("   Waiting for Streamerbot to create it...")
            return False

        # Load chat data from Streamerbot
        with open(CHAT_DATA_FILE, 'r', encoding='utf-8') as f:
            chat_data = json.load(f)

        # Convert to leaderboard format
        chatters = []
        for user_id, data in chat_data.items():
            username = data.get("Username", "Unknown")
            # Use real YouTube avatar if available, otherwise generate placeholder
            avatar = data.get("Avatar", "")
            if not avatar or avatar == "":
                avatar = generate_avatar_url(username)

            chatter = {
                "username": username,
                "messages": data.get("Messages", 0),
                "timeMinutes": data.get("TotalMinutes", 0),
                "avatar": avatar
            }
            chatters.append(chatter)

        # Create leaderboard data structure
        leaderboard_data = {
            "chatters": chatters,
            "lastUpdated": datetime.utcnow().isoformat() + "Z"
        }

        # Save to leaderboard data file
        with open(LEADERBOARD_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(leaderboard_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Updated leaderboard with {len(chatters)} chatters")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Error converting data: {e}")
        return False

def watch_mode():
    """Continuously watch for changes and update leaderboard"""
    print("🔄 Watch mode enabled - monitoring for chat updates...")
    print(f"   Chat data: {CHAT_DATA_FILE}")
    print(f"   Leaderboard: {LEADERBOARD_DATA_FILE}")
    print(f"   Update interval: {WATCH_INTERVAL}s")
    print("\nPress Ctrl+C to stop\n")

    last_modified = 0

    try:
        while True:
            # Check if file was modified
            if CHAT_DATA_FILE.exists():
                current_modified = os.path.getmtime(CHAT_DATA_FILE)

                if current_modified != last_modified:
                    print(f"📊 {datetime.now().strftime('%H:%M:%S')} - Detected changes, updating...")
                    if convert_chat_data():
                        last_modified = current_modified
            else:
                print(f"⏳ {datetime.now().strftime('%H:%M:%S')} - Waiting for chat data file...")

            time.sleep(WATCH_INTERVAL)

    except KeyboardInterrupt:
        print("\n\n👋 Stopping watch mode...")
        sys.exit(0)

def main():
    """Main entry point"""
    print("=" * 60)
    print("YouTube Chat to Leaderboard Converter")
    print("=" * 60)
    print()

    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--watch":
            watch_mode()
        elif sys.argv[1] == "--once":
            convert_chat_data()
        else:
            print("Usage:")
            print("  python convert_to_leaderboard.py --watch   (continuously monitor)")
            print("  python convert_to_leaderboard.py --once    (run once)")
            sys.exit(1)
    else:
        # Default: watch mode
        watch_mode()

if __name__ == "__main__":
    main()
