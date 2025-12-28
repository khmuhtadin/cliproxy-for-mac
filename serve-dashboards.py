#!/usr/bin/env python3
"""
Simple HTTP server to serve dashboard files
Run this if the main server doesn't have dashboard routes configured
"""

import http.server
import socketserver
import os
import sys

PORT = 8318  # Different port to avoid conflict

# Auto-detect paths
HOME = os.path.expanduser("~")
CLI_PROXY_DIR = os.path.join(HOME, ".cli-proxy-api")
DIRECTORY = os.path.join(CLI_PROXY_DIR, "static")

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers to allow API calls
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Management-Key')
        super().end_headers()

os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
    print(f"""
╔══════════════════════════════════════════════════════════╗
║     Dashboard Static File Server                        ║
╚══════════════════════════════════════════════════════════╝

🚀 Server Started!

📂 Serving from: {DIRECTORY}
🌐 Port: {PORT}

Access Dashboards:
------------------
• Dashboard v1: http://localhost:{PORT}/dashboard.html
• Dashboard v2: http://localhost:{PORT}/dashboard-v2.html ⭐

Note: Main API server should still be running on port 8317
      for API calls to work.

Press Ctrl+C to stop...
""")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped.")
        sys.exit(0)
