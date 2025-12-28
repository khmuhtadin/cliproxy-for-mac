#!/usr/bin/env python3
"""
Unified server that serves static files and proxies API requests.
Runs on port 8317 as main entry point, proxies to cliproxy on port 8316.
"""

import http.server
import socketserver
import urllib.request
import urllib.error
import subprocess
import signal
import sys
import os
import time
import atexit

# Configuration
PUBLIC_PORT = 8317      # Main entry point
BACKEND_PORT = 8316     # cliproxy-server runs here

# Auto-detect paths
HOME = os.path.expanduser("~")
CLI_PROXY_DIR = os.path.join(HOME, ".cli-proxy-api")
STATIC_DIR = os.path.join(CLI_PROXY_DIR, "static")
CLIPROXY_PATH = os.path.join(CLI_PROXY_DIR, "cliproxy-server")
CONFIG_PATH = os.path.join(CLI_PROXY_DIR, "config.yaml")

cliproxy_process = None

def start_cliproxy():
    """Start cliproxy-server on backend port"""
    global cliproxy_process

    # Modify config temporarily or use environment
    env = os.environ.copy()
    env['PORT'] = str(BACKEND_PORT)

    try:
        cliproxy_process = subprocess.Popen(
            [CLIPROXY_PATH, '-port', str(BACKEND_PORT), '-config', CONFIG_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env
        )
        print(f"   Started cliproxy-server on port {BACKEND_PORT} (PID: {cliproxy_process.pid})")
        time.sleep(1)  # Wait for startup
        return True
    except Exception as e:
        print(f"   Failed to start cliproxy: {e}")
        return False

def stop_cliproxy():
    """Stop cliproxy-server"""
    global cliproxy_process
    if cliproxy_process:
        print("\n   Stopping cliproxy-server...")
        cliproxy_process.terminate()
        try:
            cliproxy_process.wait(timeout=5)
        except:
            cliproxy_process.kill()
        cliproxy_process = None

class UnifiedHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def log_message(self, format, *args):
        # Quieter logging
        if '/v0/' in str(args) or '/v1/' in str(args):
            return  # Skip API logging
        super().log_message(format, *args)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Management-Key, Authorization')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # API requests -> proxy to backend
        if self.path.startswith('/v0/') or self.path.startswith('/v1/'):
            self.proxy_request('GET')
        # Root -> redirect to dashboard
        elif self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/dashboard.html')
            self.end_headers()
        else:
            # Static files
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

    def do_PUT(self):
        if self.path.startswith('/v0/') or self.path.startswith('/v1/'):
            self.proxy_request('PUT')
        else:
            self.send_error(404)

    def proxy_request(self, method):
        try:
            target_url = f'http://localhost:{BACKEND_PORT}{self.path}'

            # Copy headers
            headers = {}
            for key in ['X-Management-Key', 'Authorization', 'Content-Type', 'Accept']:
                if key in self.headers:
                    headers[key] = self.headers[key]

            # Get body for POST/PUT/DELETE
            data = None
            if method in ['POST', 'PUT', 'DELETE'] and 'Content-Length' in self.headers:
                content_length = int(self.headers['Content-Length'])
                data = self.rfile.read(content_length)

            req = urllib.request.Request(
                target_url,
                data=data,
                headers=headers,
                method=method
            )

            with urllib.request.urlopen(req, timeout=30) as response:
                self.send_response(response.status)

                for header, value in response.headers.items():
                    if header.lower() not in ['transfer-encoding', 'connection', 'access-control-allow-origin']:
                        self.send_header(header, value)

                self.end_headers()
                self.wfile.write(response.read())

        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(e.read())

        except urllib.error.URLError as e:
            self.send_error(503, f"Backend unavailable: {str(e.reason)}")

        except Exception as e:
            self.send_error(502, f"Proxy error: {str(e)}")

def main():
    # Register cleanup
    atexit.register(stop_cliproxy)
    signal.signal(signal.SIGTERM, lambda s, f: sys.exit(0))
    signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))

    print("""
╔══════════════════════════════════════════════════════════╗
║         Unified CLI Proxy Server                         ║
╚══════════════════════════════════════════════════════════╝
""")

    # Start backend
    print("Starting backend server...")
    if not start_cliproxy():
        print("Warning: Running without backend (API calls will fail)")

    # Start unified server
    print(f"\nStarting unified server on port {PUBLIC_PORT}...")

    with socketserver.ThreadingTCPServer(("", PUBLIC_PORT), UnifiedHandler) as httpd:
        print(f"""
Ready!

Dashboards:
  http://localhost:{PUBLIC_PORT}/              -> Dashboard (Enhanced v2)
  http://localhost:{PUBLIC_PORT}/dashboard.html
  http://localhost:{PUBLIC_PORT}/management.html

API Endpoints:
  http://localhost:{PUBLIC_PORT}/v1/...        -> Proxied to backend
  http://localhost:{PUBLIC_PORT}/v0/...        -> Proxied to backend

Press Ctrl+C to stop...
""")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

    stop_cliproxy()
    print("\nServer stopped.")

if __name__ == '__main__':
    main()
