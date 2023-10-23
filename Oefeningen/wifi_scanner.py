from scapy.all import *

# Functie om beacon frames te verwerken
def handle_packet(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode()
        bssid = packet.addr2
        print(f"SSID: {ssid}, BSSID: {bssid}")

# Draadloze interface om te scannen (pas dit aan naar jouw interface)
interface = "wlp110s0"

# Start het snifferen
sniff(iface=interface, prn=handle_packet)
