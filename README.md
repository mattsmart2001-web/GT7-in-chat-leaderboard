# Live Chat Leaderboard

A beautiful, animated HTML leaderboard for displaying your live stream chat statistics! Track who has been in your chat the longest and who has sent the most messages.

## 🤖 Automatic YouTube Tracking

**NEW!** Fully automated chat tracking for YouTube streamers using Streamerbot!

- ✅ **Zero Manual Work** - Automatically captures all chat messages
- ✅ **Real-time Updates** - Leaderboard updates as people chat
- ✅ **Easy Setup** - 3 simple steps to get started
- ✅ **Streamerbot Integration** - Works with your existing setup

**[📖 See AUTOMATION_SETUP.md for full setup guide](AUTOMATION_SETUP.md)**

### Quick Auto-Setup:
1. Add C# action to Streamerbot (captures YouTube chat)
2. Run Python converter script (formats data)
3. Open leaderboard in browser/OBS (displays rankings)

**Perfect for streamers with hundreds of chatters!**

---

## Features

- 📊 **Dual Rankings**: View top chatters by time spent OR message count
- 🎨 **Beautiful Design**: Modern glassmorphism design with smooth animations
- 🏆 **Top 3 Podium**: Special styling for the top 3 positions
- 📱 **Responsive**: Works on any screen size
- 🔄 **Real-time Updates**: Auto-refreshes data every 30 seconds
- 🎮 **OBS Ready**: Perfect for use as a browser source in OBS or streaming software

## Quick Start

### For YouTube Streamers (Recommended):
1. **Follow [AUTOMATION_SETUP.md](AUTOMATION_SETUP.md)** for automatic tracking
2. **Open `index.html`** in browser or OBS
3. **Start streaming** - leaderboard updates automatically!

### Manual Mode (Small Streams):
1. **View the Leaderboard**
   - Open `index.html` in your browser
   - Or add as a browser source in OBS

2. **Update Chat Data**
   - Open `update_data.html` to add/edit chatters
   - Or directly edit `data.json` with your chat data

## Files

- `index.html` - Main leaderboard display
- `data.json` - Chat statistics data
- `update_data.html` - Simple interface to manage chat data
- `styles.css` - Styling and animations
- `script.js` - Leaderboard logic

## Using in OBS

1. Add a **Browser Source**
2. Set the URL to the full path of `index.html`
3. Recommended size: 1920x1080 or 800x600 for sidebar
4. Check "Refresh browser when scene becomes active"
5. Set refresh rate if needed (auto-refreshes every 30s)

## Data Format

The `data.json` file stores chatter information:

```json
{
  "chatters": [
    {
      "username": "CoolViewer123",
      "messages": 450,
      "timeMinutes": 180,
      "avatar": "https://via.placeholder.com/100"
    }
  ],
  "lastUpdated": "2025-12-18T12:00:00Z"
}
```

## Customization

### Change Colors
Edit the CSS variables in `styles.css`:
```css
:root {
  --primary: #6366f1;
  --secondary: #8b5cf6;
  --gold: #fbbf24;
}
```

### Adjust Refresh Rate
Edit `script.js` and change the interval (default: 30000ms = 30s):
```javascript
setInterval(loadLeaderboardData, 30000);
```

## Automated Tracking Options

### 🎯 Recommended: Streamerbot (YouTube)

**Fully automated solution for YouTube streamers!**

See **[AUTOMATION_SETUP.md](AUTOMATION_SETUP.md)** for complete instructions.

**What you get:**
- Automatic message tracking
- Automatic time tracking
- Zero manual data entry
- Works with hundreds of chatters

**Files included:**
- `streamerbot/ChatTrackerAction.cs` - Streamerbot C# action
- `streamerbot/convert_to_leaderboard.py` - Data converter
- `streamerbot/START_TRACKER.bat` - Easy launcher
- `AUTOMATION_SETUP.md` - Complete setup guide

### Other Platform Options

- **Twitch**: Can be adapted for Twitch IRC
- **Manual Entry**: Use `update_data.html` for small streams
- **Custom Bot**: Update `data.json` programmatically with any tool

## License

MIT License - Feel free to customize and use in your streams!

## Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

Made with ❤️ for streamers
