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
import sys
from includes import banner
from includes import utils
from AttackModes import spam
from AttackModes import deauth
from includes.menu import main_menu
from rich.console import Console
from rich.panel import Panel



console = Console()




def main():
    utils.check_sudo()
    while True:
        banner.show_banner()
        choice = main_menu()

        if choice == 1:
            import os
            utils.kill_port(80)
            banner.show_banner()
            interfaces = utils.get_wifi_interfaces()
            if not interfaces:
                banner.nowifi()
            
            banner.wifi_available(interfaces)
            selected = input("👉 Enter your choice (number): ")

            try:
                if selected.strip() == "0":
                    continue  
                interface = interfaces[int(selected) - 1]
            except (IndexError, ValueError):
                banner.invalid_Selection()
                exit()

            ssid = input("📶 Enter Fake WiFi SSID: ")
            selected_template = utils.choose_template()
            if selected_template:
                print(f"✅ Selected Template: {selected_template}")
                os.system(f"bash start_portal.sh {interface} \"{ssid}\" {selected_template}")
            else:
                print("🔙 Returning to main menu...")

        elif choice == 2:
            utils.check_sudo()
            utils.check_mdk4()
            banner.show_banner()
            interfaces = utils.get_wifi_interfaces()
            if not interfaces:
                banner.nowifi()
            
            banner.wifi_available(interfaces)
            selected = input("🛜  Enter your WiFi interface (number): ").strip()
            try:
                if selected.strip() == "0":
                    continue  
                interface = interfaces[int(selected) - 1]
            except (IndexError, ValueError):
                banner.invalid_Selection()
                exit()
            
            spam.main(interface)
        elif choice == 3:
            banner.show_banner()
            interfaces = utils.get_wifi_interfaces()
            if not interfaces:
                banner.nowifi()
            
            banner.wifi_available(interfaces)
            selected = input("🛜  Enter your WiFi interface (number): ").strip()
            try:
                if selected.strip() == "0":
                    continue  
                interface = interfaces[int(selected) - 1]
            except (IndexError, ValueError):
                banner.invalid_Selection()
                exit()
            
            deauth.start_deauth(interface)

        elif choice == 5:
            banner.show_credentials()
        elif choice == 6:
            banner.bye()
            sys.exit()
        else:
            banner.not_implemented()

if __name__ == "__main__":
    main()
