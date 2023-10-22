from scapy.all import *

# Functie om beacon frames te verwerken
def verwerk_packet(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode()
        bssid = packet[Dot11].addr2
        print(f"SSID: {ssid}, BSSID: {bssid}")

interface = "00-28-F8-6C-D4-5F"

# Start het snifferen
sniff(iface=interface, prn=verwerk_packet)
