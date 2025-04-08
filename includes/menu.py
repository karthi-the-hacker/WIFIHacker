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


from rich.console import Console
from rich.table import Table
from includes import banner
from rich.prompt import IntPrompt
from includes.portal import get_credentials_json
import os

console = Console()

def clear():
    os.system("clear")

def main_menu():
   
    table = Table(title="[bold green]Main Menu[/bold green]", show_header=True, header_style="bold blue")
    table.add_column("No.", style="bold cyan")
    table.add_column("Option", style="bold white")
    table.add_row("1", "📡 Wifi Phishing")
    table.add_row("2", "📶 Wifi SPAM ")
    table.add_row("3", "🚫 Wifi DoS (Coming Soon)")
    table.add_row("4", "📘 Learn Wifi Hacking (Coming Soon)")
    table.add_row("5", "🔐 View Captured Credentials")
    table.add_row("6", "❌ Exit")
    console.print(table)
    return IntPrompt.ask("\n👉 Select an option")

