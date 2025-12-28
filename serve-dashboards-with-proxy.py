#!/usr/bin/env python3
"""
Dashboard server with API proxy to solve CORS issues
"""

import http.server
import socketserver
import urllib.request
import urllib.error
import json
import sys
from urllib.parse import urlparse, parse_qs

PORT = 8318
API_PORT = 8317

# Auto-detect paths
import os
HOME = os.path.expanduser("~")
CLI_PROXY_DIR = os.path.join(HOME, ".cli-proxy-api")
STATIC_DIR = os.path.join(CLI_PROXY_DIR, "static")

class DashboardProxyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Management-Key, Authorization')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        # Proxy API requests
        if self.path.startswith('/v0/') or self.path.startswith('/v1/'):
            self.proxy_request('GET')
        else:
            # Serve static files
            super().do_GET()
    
    def do_POST(self):
        if self.path.startswith('/v0/') or self.path.startswith('/v1/'):
            self.proxy_request('POST')
        else:
            self.send_error(404)
    
    def do_DELETE(self):
        if self.path.startswith('/v0/') or self.path.startswith('/v1/'):
            self.proxy_request('DELETE')
        else:
            self.send_error(404)
    
    def proxy_request(self, method):
        try:
            # Build target URL
            target_url = f'http://localhost:{API_PORT}{self.path}'
            
            # Get headers from original request
            headers = {}
            if 'X-Management-Key' in self.headers:
                headers['X-Management-Key'] = self.headers['X-Management-Key']
            if 'Authorization' in self.headers:
                headers['Authorization'] = self.headers['Authorization']
            if 'Content-Type' in self.headers:
                headers['Content-Type'] = self.headers['Content-Type']
            
            # Get body for POST/DELETE
            data = None
            if method in ['POST', 'DELETE'] and 'Content-Length' in self.headers:
                content_length = int(self.headers['Content-Length'])
                data = self.rfile.read(content_length)
            
            # Make request to API server
            req = urllib.request.Request(
                target_url,
                data=data,
                headers=headers,
                method=method
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                # Send response
                self.send_response(response.status)
                
                # Copy response headers
                for header, value in response.headers.items():
                    if header.lower() not in ['transfer-encoding', 'connection']:
                        self.send_header(header, value)
                
                self.end_headers()
                
                # Copy response body
                self.wfile.write(response.read())
        
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())
        
        except Exception as e:
            print(f"Proxy error: {e}")
            self.send_error(502, f"Bad Gateway: {str(e)}")

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), DashboardProxyHandler) as httpd:
        print(f"""
╔══════════════════════════════════════════════════════════╗
║     Dashboard Server with API Proxy                     ║
╚══════════════════════════════════════════════════════════╝

🚀 Server Started!

📂 Static Files: {STATIC_DIR}
🌐 Dashboard Port: {PORT}
🔌 API Proxy: localhost:{API_PORT} → localhost:{PORT}

Access Dashboards:
------------------
• Dashboard v2: http://localhost:{PORT}/dashboard-v2.html ⭐
• Dashboard v1: http://localhost:{PORT}/dashboard.html

API Proxy Active:
-----------------
All /v0/* and /v1/* requests are proxied to port {API_PORT}
CORS issues automatically handled!

Press Ctrl+C to stop...
""")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped.")
            sys.exit(0)
