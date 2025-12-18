// Current leaderboard mode: 'messages' or 'time'
let currentMode = 'messages';
let leaderboardData = null;

// Format time in minutes to human-readable format
function formatTime(minutes) {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;

    if (hours > 0) {
        return `${hours}h ${mins}m`;
    }
    return `${mins}m`;
}

// Format numbers with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Format date for last updated
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Load leaderboard data from JSON file
async function loadLeaderboardData() {
    try {
        const response = await fetch('data.json');
        leaderboardData = await response.json();

        // Update last updated timestamp
        document.getElementById('lastUpdated').textContent = formatDate(leaderboardData.lastUpdated);

        // Update footer stats
        updateFooterStats();

        // Render the leaderboard
        renderLeaderboard();
    } catch (error) {
        console.error('Error loading leaderboard data:', error);
        document.getElementById('leaderboard').innerHTML = `
            <div style="text-align: center; padding: 3rem; color: var(--text-secondary);">
                <h2>Unable to load leaderboard data</h2>
                <p>Please make sure data.json is available</p>
            </div>
        `;
    }
}

// Update footer statistics
function updateFooterStats() {
    if (!leaderboardData) return;

    const totalChatters = leaderboardData.chatters.length;
    const totalMessages = leaderboardData.chatters.reduce((sum, chatter) => sum + chatter.messages, 0);
    const totalMinutes = leaderboardData.chatters.reduce((sum, chatter) => sum + chatter.timeMinutes, 0);
    const totalHours = Math.round(totalMinutes / 60);

    document.getElementById('totalChatters').textContent = formatNumber(totalChatters);
    document.getElementById('totalMessages').textContent = formatNumber(totalMessages);
    document.getElementById('totalTime').textContent = formatNumber(totalHours);
}

// Render the leaderboard based on current mode
function renderLeaderboard() {
    if (!leaderboardData) return;

    const leaderboardContainer = document.getElementById('leaderboard');

    // Sort chatters based on current mode
    let sortedChatters = [...leaderboardData.chatters];

    if (currentMode === 'messages') {
        sortedChatters.sort((a, b) => b.messages - a.messages);
    } else {
        sortedChatters.sort((a, b) => b.timeMinutes - a.timeMinutes);
    }

    // Clear existing content
    leaderboardContainer.innerHTML = '';

    // Create leaderboard items
    sortedChatters.forEach((chatter, index) => {
        const rank = index + 1;
        const item = createLeaderboardItem(chatter, rank);

        // Add animation delay based on position
        item.style.animationDelay = `${index * 0.05}s`;

        leaderboardContainer.appendChild(item);
    });
}

// Create a single leaderboard item
function createLeaderboardItem(chatter, rank) {
    const item = document.createElement('div');
    item.className = `leaderboard-item rank-${rank}`;

    // Determine primary stat based on mode
    const primaryStat = currentMode === 'messages'
        ? formatNumber(chatter.messages)
        : formatTime(chatter.timeMinutes);

    // Medal emoji for top 3
    const medals = ['🥇', '🥈', '🥉'];
    const rankDisplay = rank <= 3 ? medals[rank - 1] : `#${rank}`;

    item.innerHTML = `
        <div class="rank-badge">${rankDisplay}</div>
        <img src="${chatter.avatar}" alt="${chatter.username}" class="avatar">
        <div class="user-info">
            <div class="username">${chatter.username}</div>
            <div class="stats">
                <div class="stat">
                    <span class="stat-icon">💬</span>
                    <span>${formatNumber(chatter.messages)} messages</span>
                </div>
                <div class="stat">
                    <span class="stat-icon">⏱️</span>
                    <span>${formatTime(chatter.timeMinutes)} in chat</span>
                </div>
            </div>
        </div>
        <div class="primary-stat">${primaryStat}</div>
    `;

    return item;
}

// Switch between leaderboard modes
function switchMode(mode) {
    if (mode === currentMode) return;

    currentMode = mode;

    // Update button states
    document.querySelectorAll('.toggle-btn').forEach(btn => {
        if (btn.dataset.mode === mode) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // Re-render leaderboard
    renderLeaderboard();
}

// Initialize event listeners
function initializeEventListeners() {
    document.querySelectorAll('.toggle-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            switchMode(btn.dataset.mode);
        });
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
    loadLeaderboardData();

    // Auto-refresh every 30 seconds
    setInterval(loadLeaderboardData, 30000);
});
