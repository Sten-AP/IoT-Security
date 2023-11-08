from networksettings import change_channel, network_to_managed, network_to_monitor
from scapy.all import AsyncSniffer, IP, Dot11Beacon, Dot11, Dot11Elt, Dot11EltRates, Dot11EltDSSSet, Dot11EltCountry, Dot11EltERP, Dot11EltHTCapabilities, Dot11EltVendorSpecific, Dot11EltRSN
from threading import Thread
from subprocess import PIPE, Popen
import time
from datetime import datetime
import threading
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = BASE_DIR + "/data"

INTERFACE = "wlp110s0"
INTERFACE_MON = f"{INTERFACE}mon"

try:
    network_to_managed(INTERFACE_MON)
except:
    print("Netwerk kaart staat al in managed.")

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
    global channel_nr, dir
    if packet.haslayer(Dot11Beacon):
        # data = packet.show()
        # print(data)
        ssid = str(packet).split("'")
        ssid.pop(2)
        ssid.pop(0)
        ssid = ssid[0]
        
        print(f"-\t-\t-\t-\t-\t-{ssid}-\t-\t-\t-\t-\t-")
        # if not os.path.exists(f"{DATA_DIR}/{dir}/channel_{channel_nr}"):
        #     os.mkdir(f"{DATA_DIR}/{dir}/channel_{channel_nr}")
        
        # file = open(DATA_DIR + f"/{dir}/channel_{channel_nr}/{ssid}.txt", "w")
        # file.write(data)
        
        # print(packet[Dot11EltVendorSpecific].ID)
        # addr = packet.addr3
        # print(f"naam: {ssid}\tMAC-addres: {addr}")
        # file.write(f"[{datetime.now().strftime('%H:%M:%S')}]\tnaam: {ssid}\t  MAC-addres: {addr}\n")
    # if packet.haslayer(Dot11) and packet[Dot11].type == 0 and packet[Dot11].subtype == 8:
        # print('[>]AP',packet[Dot11].addr2,'SSID',packet[Dot11].info)

    # bssid = packet.addr2
    # ssid = packet.info.decode()
    # print(f"SSID: {ssid}, BSSID: {bssid}")



netwerk_sniffer = AsyncSniffer(iface=INTERFACE_MON, prn=handle_packet)
locky = threading.Lock()
    
def main():
        network_to_monitor(INTERFACE)
    # while True:
        global channel_nr, dir
        for channel in usable_channels:
            channel_nr = channel[0]
            if channel[1] <= 2.472:
                dir = "2.4GHz"
            elif channel[1] <= 5.700:
                dir = "5GHz"
            elif channel[1] <= 6.435:
                dir = "6GHz"
            
            t = Thread(target=change_channel(INTERFACE_MON, channel[0]))
            t.daemon = True
            
            netwerk_sniffer.start()
            locky.acquire()
            t.start
            time.sleep(2)
            locky.release()
        network_to_managed(INTERFACE_MON)
            


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        netwerk_sniffer.stop()
        network_to_managed(INTERFACE_MON)
        