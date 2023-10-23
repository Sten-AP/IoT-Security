from scapy.all import *

def handle_packet(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode()
        bssid = packet.addr2
        print(f"SSID: {ssid}, BSSID: {bssid}")

interface = "wlp110s0"

sniff(iface=interface, prn=handle_packet)