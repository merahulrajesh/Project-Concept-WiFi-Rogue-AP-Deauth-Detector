# WiFi Sentinel: Wireless Intrusion Detection System (WIDS)

An automated, lightweight Python security tool designed to monitor local wireless space for malicious network activity like Deauthentication floods and Evil Twin (Rogue AP) deployments.

## 🚀 Features
- **Real-time Packet Sniffing:** Leverages raw 802.11 frame processing via Scapy.
- **Deauth Detection:** Instantly flags high-velocity deauthentication frames signaling a network disruption attack.
- **Rogue AP Mitigation:** Cross-checks BSSID fingerprints against authorized configurations to flag spoofed SSIDs.
- **Telegram Integration:** Pushes instant telemetry alerts directly to an incident responder's phone.

## 🛠️ Prerequisites & Setup
1. **Wireless Hardware:** A wireless network adapter supporting **Monitor Mode** and packet injection (e.g., Alfa AWUS036ACM).
2. **Operating System:** Linux (Kali Linux or Parrot OS recommended).

### Installation
```bash
# Clone the repository
git clone 
[https://github.com/merahulrajesh/Project-Concept-WiFi-Rogue-AP-Deauth-Detector.git]
# Install requirements
pip3 install -r requirements.txt
