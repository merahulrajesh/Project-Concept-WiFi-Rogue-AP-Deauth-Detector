
import os
import sys
import requests
from scapy.all import *


TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
HOME_SSID = "YOUR_HOME_WIFI_NAME"
ORIGINAL_BSSID = "aa:bb:cc:dd:ee:ff" 

def send_telegram_alert(message):
    """Sends a real-time critical alert notification to your Telegram channel/chat."""
    if TELEGRAM_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
        return 
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"[-] Failed to send Telegram alert: {e}")

def packet_handler(pkt):
    
    if pkt.haslayer(Dot11):
        
       
        if pkt.type == 0 and pkt.subtype == 12:
            attacker = pkt.addr2
            victim = pkt.addr1
            alert_msg = f"[🚨 ALERT] WiFi Deauth Attack Detected!\nTarget MAC: {victim}\nSource/Attacker MAC: {attacker}"
            print(alert_msg)
            send_telegram_alert(alert_msg)
            
        
        elif pkt.type == 0 and pkt.subtype == 8:
            try:
                ssid = pkt.info.decode('utf-8', errors='ignore')
                bssid = pkt.addr3
                
               
                if ssid == HOME_SSID and bssid.lower() != ORIGINAL_BSSID.lower():
                    alert_msg = f"[⚠️ WARNING] Evil Twin / Rogue AP Detected!\nSSID: {ssid}\nFake BSSID (MAC): {bssid}\nExpected BSSID: {ORIGINAL_BSSID}"
                    print(alert_msg)
                    send_telegram_alert(alert_msg)
            except Exception:
                pass

def main():
   
    if os.geteuid() != 0:
        print("[-] Error: This script must be executed with sudo privileges.")
        sys.exit(1)
        
    interface = input("Enter your Monitor Mode Interface (e.g., wlan0mon): ")
    
    print("\n" + "="*50)
    print(f"📡 WiFi Sentinel Active on {interface}...")
    print(f"Monitoring for Deauth floods and Rogue APs targeting '{HOME_SSID}'")
    print("="*50 + "\n")
    
   
    sniff(iface=interface, prn=packet_handler, store=0)

if __name__ == "__main__":
    main()
