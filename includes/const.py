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


def paths():

    redirect_paths = [
                "/", "/index.html",
                "/generate_204", "/gen_204",
                "/mobile/status.php",                          # Samsung-specific
                "/hotspot-detect.html",                        # Apple
                "/ncsi.txt", "/connecttest.txt", "/redirect",  # Windows & others
                "/success.txt", "/favicon.ico",
                "/connectivity-check.html"
            ]
    return redirect_paths


def credfile():
    CRED_FILE = "/../../includes/config/credentials.json"
    return CRED_FILE

def port():
    PORT = 80
    return PORT