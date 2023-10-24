from scapy.all import sniff, AsyncSniffer, Dot11
from scapy.layers import dot11
from threading import Thread
from subprocess import PIPE, Popen

import shlex
import time
import threading
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = BASE_DIR + "/data"

locky = threading.Lock()
channels = 233
interface = "wlp110s0"


if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)
    os.mkdir(f"{DATA_DIR}/2.4GHz")
    os.mkdir(f"{DATA_DIR}/5GHz")
    os.mkdir(f"{DATA_DIR}/6GHz")


stdout = Popen('iwlist ' + interface + ' channel', shell=True, stdout=PIPE).stdout
output = str(stdout.read()).replace(' ', '').split("\\n")
output.pop(0)
for i in range(3):
    output.pop(len(output)-1)

usable_channels = []
for out in output:
	split = out.split(":")
	usable_channels.append([int(split[0][7:]), float(split[1][:-3])])

def handle_packet(packet):
    global file
    if packet.haslayer(Dot11):
        print(packet)
        file.write(str(packet)+"\n")
    # bssid = packet.addr2
    # ssid = packet.info.decode()
    # print(f"SSID: {ssid}, BSSID: {bssid}")

def Change_Freq_channel(channel):
    print(f'Channel: {channel}')
    command = f'iwconfig {interface} channel {channel}'
    command = shlex.split(command)
    Popen(command, shell=False)


netwerk_sniffer = AsyncSniffer(iface=interface, prn=handle_packet)

try:
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
            
            t = Thread(target=Change_Freq_channel, args=(channel[0],))
            t.daemon = True
            
            netwerk_sniffer.start()
            locky.acquire()
            t.start
            time.sleep(2)
            locky.release()
            netwerk_sniffer.stop()
                

            
except KeyboardInterrupt:
    locky.release()
    netwerk_sniffer.stop()