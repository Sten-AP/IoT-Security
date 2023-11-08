from netwerk_settings import change_channel, network_to_managed, network_to_monitor
from scapy.all import AsyncSniffer, Dot11Beacon
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
        ssid = str(packet).split("'")
        ssid.pop(2)
        ssid.pop(0)
        ssid = ssid[0]
        
        if not os.path.exists(f"{DATA_DIR}/{dir}/channel_{channel_nr}"):
            os.mkdir(f"{DATA_DIR}/{dir}/channel_{channel_nr}")
        
        if ssid != "":
            print(f"--- {ssid} ---")
            file = open(DATA_DIR + f"/{dir}/channel_{channel_nr}/{ssid}.txt", "a")
            file.write(str(packet.show)+"\n")

    
def main():
    network_to_monitor(INTERFACE)
    antwoord = ""
    while antwoord.lower() != "q":
        antwoord = input("(q)uit, (s)cannen: ")
        
        if antwoord.lower() == "s":
            seconden = input("Hoeveel seconden scannen per kanaal: ")
            
            global channel_nr, dir
            for channel in usable_channels:
                if channel[1] <= 2.472:
                    dir = "2.4GHz"
                elif channel[1] <= 5.700:
                    dir = "5GHz"
                elif channel[1] <= 6.435:
                    dir = "6GHz"
                channel_nr = channel[0]
                
                t = Thread(target=change_channel(INTERFACE_MON, channel[0]))
                t.daemon = True
                
                netwerk_sniffer.start()
                locky.acquire()
                t.start
                time.sleep(int(seconden))
                locky.release()
                
        elif antwoord.lower() not in ["q", "s"]:
            print("Dit bestaat niet.")
            
    network_to_managed(INTERFACE_MON)
            

if __name__ == "__main__":
    try:
        netwerk_sniffer = AsyncSniffer(iface=INTERFACE_MON, prn=handle_packet)
        locky = threading.Lock()
        main()
    except KeyboardInterrupt:
        netwerk_sniffer.stop()
        network_to_managed(INTERFACE_MON)
        