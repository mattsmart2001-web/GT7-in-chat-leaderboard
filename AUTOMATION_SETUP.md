# 🤖 Automatic Chat Tracking Setup Guide

This guide will help you set up **automatic YouTube chat tracking** using Streamerbot. Once configured, your leaderboard will update automatically as people chat!

---

## 📋 Prerequisites

- ✅ **Streamerbot** installed and connected to YouTube
- ✅ **Python 3.7+** installed ([Download Python](https://www.python.org/downloads/))
- ✅ YouTube channel connected to Streamerbot

---

## 🚀 Quick Setup (3 Steps)

### Step 1: Configure Streamerbot Action

1. **Open Streamerbot**

2. **Create a new Action:**
   - Click `Actions` tab
   - Click `Add` button
   - Name it: `YouTube Chat Tracker`

3. **Add C# Code:**
   - In the action, click `Add Sub-Action`
   - Select `Core` → `Execute Code` → `Execute Code (C# Code)`
   - Open the file: `streamerbot/ChatTrackerAction.cs`
   - Copy ALL the code
   - Paste it into Streamerbot's code editor

4. **Update the file path in the code:**
   ```csharp
   // Line 22 - CHANGE THIS to match your actual path!
   private string dataFilePath = @"C:\Users\YourUsername\GT7-in-chat-leaderboard\streamerbot\chat_data.json";
   ```

   Example:
   ```csharp
   private string dataFilePath = @"C:\Users\John\Documents\GT7-in-chat-leaderboard\streamerbot\chat_data.json";
   ```

5. **Compile the code:**
   - Click `Compile` button in Streamerbot
   - Make sure it says "Compiled successfully"

6. **Link to YouTube Events:**
   - Go to `Settings` → `Events` → `YouTube`
   - Find `Message` event
   - Link it to your `YouTube Chat Tracker` action
   - ✅ Done!

---

### Step 2: Start the Converter Script

The Python script converts Streamerbot data to leaderboard format.

**Option A: Simple Double-Click (Windows)**
```
Double-click: START_TRACKER.bat
```
That's it! Keep this window open while streaming.

**Option B: Manual Command**
```bash
cd streamerbot
python convert_to_leaderboard.py --watch
```

The script will:
- ✅ Monitor for new chat data
- ✅ Update `data.json` automatically every 5 seconds
- ✅ Keep running until you stop it

---

### Step 3: Open Your Leaderboard

Just open `index.html` in a browser or add it to OBS!

```
File → Open → index.html
```

The leaderboard will auto-refresh every 30 seconds to show new data.

---

## 📊 How It Works

```
YouTube Chat
    ↓
Streamerbot (captures messages)
    ↓
chat_data.json (raw tracking data)
    ↓
Python Script (converts format)
    ↓
data.json (leaderboard data)
    ↓
index.html (displays leaderboard)
```

---

## 🎮 Using in OBS

### Add as Browser Source

1. **Add Browser Source:**
   - Sources → Add → Browser
   - Name: `Chat Leaderboard`

2. **Configure:**
   - **URL:** `file:///C:/Users/YourName/GT7-in-chat-leaderboard/index.html`
   - **Width:** 800 (or 1920 for full screen)
   - **Height:** 600 (or 1080 for full screen)
   - ✅ Check "Refresh browser when scene becomes active"

3. **Position:**
   - Drag to desired location
   - Resize as needed
   - Consider using a sidebar layout

### Tips for OBS:
- Use **Chroma Key** if you want transparency (though the design already has a dark background)
- Set **Refresh rate** to 30-60 seconds
- Add to a **Scene Collection** for easy reuse

---

## 🔧 Customization

### Change Update Speed

**Python Script (file monitoring):**
Edit `convert_to_leaderboard.py`:
```python
WATCH_INTERVAL = 5  # Change to 10 for slower, 2 for faster
```

**Leaderboard Display (auto-refresh):**
Edit `script.js`:
```javascript
setInterval(loadLeaderboardData, 30000);  // 30000 = 30 seconds
```

### Change Colors

Edit `styles.css`:
```css
:root {
    --primary: #6366f1;     /* Change to your color */
    --secondary: #8b5cf6;
    --gold: #fbbf24;
}
```

### Filter Out Bots

Edit `convert_to_leaderboard.py` and add:
```python
# Add after line 50
IGNORE_USERS = ["Nightbot", "StreamElements", "Moobot"]

# Modify the conversion loop:
for user_id, data in chat_data.items():
    username = data.get("Username", "Unknown")
    if username in IGNORE_USERS:
        continue  # Skip this user
    # ... rest of code
```

---

## ❓ Troubleshooting

### Streamerbot isn't tracking messages

**Check:**
- ✅ Streamerbot is connected to YouTube
- ✅ YouTube events are enabled in Settings
- ✅ Action is linked to `YouTube Message` event
- ✅ File path in C# code is correct
- ✅ Check Streamerbot logs for errors

**Test:**
- Send a message in your YouTube chat
- Check Streamerbot's action log
- Look for "ChatTracker: Updated [username]"

### Python script not working

**Error: "Python not found"**
```bash
# Install Python from python.org
# Make sure to check "Add to PATH" during installation
```

**Error: "File not found"**
- Check that `chat_data.json` exists in `streamerbot/` folder
- Make sure Streamerbot created the file (send a test chat message)
- Verify the path in the C# code matches your actual folder

**Script runs but data.json not updating**
- Check Python console for error messages
- Verify `chat_data.json` has content
- Try running with `--once` flag to test: `python convert_to_leaderboard.py --once`

### Leaderboard shows old data

**Solutions:**
- Hard refresh browser: `Ctrl + F5`
- Check that `data.json` has recent `lastUpdated` timestamp
- Make sure Python script is running
- Check browser console (F12) for errors

### Time tracking seems wrong

This is expected! Time tracking is estimated based on:
- First time user was seen
- Last message they sent

It's not perfect but gives a good approximation. For exact tracking, you'd need YouTube API access (more complex).

---

## 🎯 Pro Tips

### Tip 1: Start Everything Together
Create a batch file that starts both Streamerbot and the Python script:

```batch
@echo off
start "" "C:\Path\To\Streamer.bot.exe"
timeout /t 5
start "" python "C:\Path\To\convert_to_leaderboard.py" --watch
```

### Tip 2: Run as Startup
- Add `START_TRACKER.bat` to Windows Startup folder
- Windows + R → `shell:startup` → paste shortcut

### Tip 3: Use Two Monitors
- Monitor 1: OBS with leaderboard overlay
- Monitor 2: Python console to monitor updates

### Tip 4: Reset Stats Between Streams
Before each stream:
```bash
# Delete old data to start fresh
del streamerbot\chat_data.json
```

Or keep it to track all-time stats!

---

## 🔐 Privacy & Data

**What data is stored:**
- Username
- Message count
- Approximate time in chat
- User ID (YouTube)

**Where:**
- Locally on your computer only
- No cloud uploads
- No personal information

**GDPR Compliance:**
- Users can request deletion
- Simply remove their entry from `chat_data.json`

---

## 📞 Need Help?

If you encounter issues:

1. Check the **Troubleshooting** section above
2. Verify all paths are correct
3. Test each component individually
4. Check Streamerbot logs
5. Look at Python console output

---

## 🚀 Advanced: StreamElements Integration

If you want to use StreamElements as well, you can:

1. Use StreamElements Custom Overlay to display `data.json`
2. Use SE API to fetch chat data (requires API key)
3. Combine both tracking methods for redundancy

*This is optional and more advanced - the Streamerbot method is recommended for simplicity.*

---

## ✅ Final Checklist

Before your stream:

- [ ] Streamerbot is running and connected
- [ ] C# action is compiled and linked to YouTube events
- [ ] Python script is running (`START_TRACKER.bat`)
- [ ] `index.html` opens and shows the leaderboard
- [ ] OBS browser source is configured
- [ ] Sent test message to verify tracking works
- [ ] Leaderboard updates within ~30 seconds

**You're all set! Happy streaming! 🎮📊**

---

## 📝 Summary

```
1. Configure Streamerbot C# action     → Captures chat
2. Start Python converter script       → Formats data
3. Open leaderboard in browser/OBS     → Shows rankings
```

**That's it! Fully automatic YouTube chat tracking!**
