#!/usr/bin/env python3
"""
Simple HTTP server for the leaderboard
Run this to view the leaderboard in your browser without CORS issues
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configuration
PORT = 8000
HOST = 'localhost'

# Change to script directory
os.chdir(Path(__file__).parent)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler with better CORS support"""

    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Cleaner logging
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    print("=" * 60)
    print("🎮 GT7 Chat Leaderboard Server")
    print("=" * 60)
    print(f"\n✅ Server starting on http://{HOST}:{PORT}")
    print(f"📁 Serving files from: {os.getcwd()}")
    print("\n📖 Instructions:")
    print(f"   1. Open your browser to: http://{HOST}:{PORT}")
    print(f"   2. Or use this URL in OBS Browser Source")
    print(f"\n⏹️  Press Ctrl+C to stop the server\n")
    print("=" * 60 + "\n")

    # Create server
    with socketserver.TCPServer((HOST, PORT), CustomHandler) as httpd:
        # Open browser automatically
        try:
            webbrowser.open(f'http://{HOST}:{PORT}')
            print(f"🌐 Browser opened automatically\n")
        except:
            print(f"⚠️  Could not open browser automatically")
            print(f"   Please open: http://{HOST}:{PORT}\n")

        # Serve forever
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped")
            print("=" * 60)

if __name__ == "__main__":
    main()
