from scapy.all import sniff, AsyncSniffer, Dot11
# from scapy.layers import dot11
from threading import Thread
import subprocess,shlex,time
import threading
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = BASE_DIR + "/data"

channels = 233
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

locky = threading.Lock()

def handle_packet(packet):
    global file
    if packet.haslayer(Dot11):
        print(packet)
        file.write(str(packet)+"\n")
    # bssid = packet.addr2
    # ssid = packet.info.decode()
    # print(f"SSID: {ssid}, BSSID: {bssid}")

def Change_Freq_channel(channel):
    print('Channel:',str(channel))
    command = f'iwconfig {interface} channel '+str(channel)
    command = shlex.split(command)
    try:
        subprocess.Popen(command, shell=False)
    except Exception as e:
        print(e)
        
interface = "wlp110s0"
netwerk_sniffer = AsyncSniffer(iface=interface, prn=handle_packet)

try:
    # while True:
        for i in range(1, channels+1):
                t = Thread(target=Change_Freq_channel, args=(i,))
                t.daemon = True
                global file
                file = open(DATA_DIR + f"/channel_{i}.txt", "w")
                netwerk_sniffer.start()
                locky.acquire()
                t.start()
                time.sleep(3)
                locky.release()
                netwerk_sniffer.stop()
                

            
except KeyboardInterrupt:
    locky.release()
    netwerk_sniffer.stop()