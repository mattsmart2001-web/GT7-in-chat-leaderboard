using System;
using System.IO;
using System.Collections.Generic;
using Newtonsoft.Json;

// ===================================================================
// STREAMERBOT C# ACTION - YouTube Chat Tracker
// ===================================================================
// This action tracks YouTube chat messages and user presence time
//
// HOW TO USE:
// 1. In Streamerbot, create a new Action
// 2. Add "Execute Code" -> "C# Code"
// 3. Paste this entire code
// 4. Link this action to "YouTube Message" event
// 5. Also link to "YouTube User First Seen" event (optional)
// ===================================================================

public class CPHInline
{
    // Path where chat data is stored (UPDATE THIS PATH!)
    private string dataFilePath = @"C:\Users\YourUsername\GT7-in-chat-leaderboard\streamerbot\chat_data.json";

    public bool Execute()
    {
        try
        {
            // Get user info from YouTube chat event
            string username = args.ContainsKey("userName") ? args["userName"].ToString() : "";
            string userId = args.ContainsKey("userId") ? args["userId"].ToString() : "";
            string message = args.ContainsKey("message") ? args["message"].ToString() : "";
            string avatarUrl = args.ContainsKey("userProfileImageUrl") ? args["userProfileImageUrl"].ToString() : "";

            if (string.IsNullOrEmpty(username))
            {
                CPH.LogInfo("ChatTracker: No username found in event");
                return false;
            }

            // Load existing data
            Dictionary<string, ChatterData> chatters = LoadChatData();

            // Update or create chatter data
            if (!chatters.ContainsKey(userId))
            {
                chatters[userId] = new ChatterData
                {
                    UserId = userId,
                    Username = username,
                    Avatar = avatarUrl,
                    Messages = 0,
                    FirstSeen = DateTime.UtcNow,
                    LastSeen = DateTime.UtcNow,
                    TotalMinutes = 0
                };
                CPH.LogInfo($"ChatTracker: New chatter detected - {username}");
            }

            // Update message count and last seen
            chatters[userId].Messages++;
            chatters[userId].LastSeen = DateTime.UtcNow;
            chatters[userId].Username = username; // Update username in case it changed

            // Update avatar if available
            if (!string.IsNullOrEmpty(avatarUrl))
            {
                chatters[userId].Avatar = avatarUrl;
            }

            // Calculate time spent (rough estimate based on activity)
            TimeSpan timeSinceFirst = DateTime.UtcNow - chatters[userId].FirstSeen;
            chatters[userId].TotalMinutes = (int)timeSinceFirst.TotalMinutes;

            // Save updated data
            SaveChatData(chatters);

            CPH.LogInfo($"ChatTracker: Updated {username} - Messages: {chatters[userId].Messages}, Time: {chatters[userId].TotalMinutes}m");

            return true;
        }
        catch (Exception ex)
        {
            CPH.LogError($"ChatTracker Error: {ex.Message}");
            return false;
        }
    }

    private Dictionary<string, ChatterData> LoadChatData()
    {
        try
        {
            if (File.Exists(dataFilePath))
            {
                string json = File.ReadAllText(dataFilePath);
                return JsonConvert.DeserializeObject<Dictionary<string, ChatterData>>(json)
                    ?? new Dictionary<string, ChatterData>();
            }
        }
        catch (Exception ex)
        {
            CPH.LogError($"ChatTracker: Error loading data - {ex.Message}");
        }

        return new Dictionary<string, ChatterData>();
    }

    private void SaveChatData(Dictionary<string, ChatterData> chatters)
    {
        try
        {
            // Ensure directory exists
            string directory = Path.GetDirectoryName(dataFilePath);
            if (!Directory.Exists(directory))
            {
                Directory.CreateDirectory(directory);
            }

            string json = JsonConvert.SerializeObject(chatters, Formatting.Indented);
            File.WriteAllText(dataFilePath, json);
        }
        catch (Exception ex)
        {
            CPH.LogError($"ChatTracker: Error saving data - {ex.Message}");
        }
    }
}

public class ChatterData
{
    public string UserId { get; set; }
    public string Username { get; set; }
    public string Avatar { get; set; }
    public int Messages { get; set; }
    public DateTime FirstSeen { get; set; }
    public DateTime LastSeen { get; set; }
    public int TotalMinutes { get; set; }
}
