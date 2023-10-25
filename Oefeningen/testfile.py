from scapy.all import sniff
import os

interface_mon = "wlp110s0"

os.system(f"sudo -S airmon-ng check kill")
os.system(f"sudo airmon-ng start {interface_mon} ")
os.system(f"sudo iwconfig")

# Capture Wi-Fi packets with a filter for beacon frames
packets = sniff(iface=interface_mon, filter="type mgt subtype beacon", count=10)
# Extract the MAC address and signal strength (RSSI) of each access point
access_points = []
for pkt in packets:
    mac = pkt.addr2
    rssi = -(256-ord(pkt.notdecoded[-2:-1]))
    access_points.append({'mac': mac, 'rssi': rssi})

print(access_points)