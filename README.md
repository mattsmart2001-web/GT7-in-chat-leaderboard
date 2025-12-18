# Live Chat Leaderboard

A beautiful, animated HTML leaderboard for displaying your live stream chat statistics! Track who has been in your chat the longest and who has sent the most messages.

## Features

- 📊 **Dual Rankings**: View top chatters by time spent OR message count
- 🎨 **Beautiful Design**: Modern glassmorphism design with smooth animations
- 🏆 **Top 3 Podium**: Special styling for the top 3 positions
- 📱 **Responsive**: Works on any screen size
- 🔄 **Real-time Updates**: Auto-refreshes data every 30 seconds
- 🎮 **OBS Ready**: Perfect for use as a browser source in OBS or streaming software

## Quick Start

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

## Integration with Chat Bots

You can integrate this with popular chat bots to automatically track data:

- **Nightbot**: Use custom commands to log chat activity
- **StreamElements**: Track viewer engagement
- **Custom Bot**: Update `data.json` programmatically

## License

MIT License - Feel free to customize and use in your streams!

## Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

Made with ❤️ for streamers
