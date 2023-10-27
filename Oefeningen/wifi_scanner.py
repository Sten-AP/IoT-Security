from scapy.all import AsyncSniffer, Dot11Beacon, Dot11
from threading import Thread
from subprocess import PIPE, Popen, run
import time
from datetime import datetime
import threading
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = BASE_DIR + "/data"

INTERFACE = "wlp110s0"
INTERFACE_MON = f"{INTERFACE}mon"


if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)
    os.mkdir(f"{DATA_DIR}/2.4GHz")
    os.mkdir(f"{DATA_DIR}/5GHz")
    os.mkdir(f"{DATA_DIR}/6GHz")

stdout = Popen(f'iwlist {INTERFACE} channel', shell=True, stdout=PIPE).stdout
output = str(stdout.read()).replace(' ', '').split("\\n")
output.pop(0)
for i in range(3):
    output.pop(len(output)-1)

usable_channels = []
for out in output:
	split = out.split(":")
	usable_channels.append([int(split[0][7:]), float(split[1][:-3])])



def handle_packet(packet):
    # global file
    if packet.haslayer(Dot11Beacon):
        print(packet)
        file.write(f"[>]{datetime.now().strftime('%H-%M-%S')}: {packet[Dot11Beacon]}\n")
    # if packet.haslayer(Dot11) and packet[Dot11].type == 0 and packet[Dot11].subtype == 8:
        # print('[>]AP',packet[Dot11].addr2,'SSID',packet[Dot11].info)

    # bssid = packet.addr2
    # ssid = packet.info.decode()
    # print(f"SSID: {ssid}, BSSID: {bssid}")

def change_channel(channel):
    print(f'Channel: {channel}')
    Popen(f'iwconfig {INTERFACE_MON} channel {channel}', shell=True)

def network_to_monitor():
    run("sudo airmon-ng check kill", shell=True)
    run(f"sudo airmon-ng start {INTERFACE}", shell=True)

def network_to_managed():
    run(f"sudo airmon-ng stop {INTERFACE_MON}", shell=True)
    run("sudo systemctl start NetworkManager", shell=True)

netwerk_sniffer = AsyncSniffer(iface=INTERFACE_MON, prn=handle_packet)
locky = threading.Lock()
    
def main():
        network_to_monitor()
    # while True:
        for channel in usable_channels:
            if channel[1] <= 2.472:
                dir = "2.4GHz"
            elif channel[1] <= 5.700:
                dir = "5GHz"
            elif channel[1] <= 6.435:
                dir = "6GHz"
            
            global file
            file = open(DATA_DIR + f"/{dir}/channel_{channel[0]}.txt", "w")
            
            t = Thread(target=change_channel(channel[0]))
            t.daemon = True
            
            netwerk_sniffer.start()
            locky.acquire()
            t.start
            time.sleep(5)
            locky.release()
        network_to_managed()
            


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        netwerk_sniffer.stop()
        network_to_managed()
        