# Logboek week 5

_Sten Hulsbergen_

## Voortgang

Voor de opdracht van week 5 heb ik gekozen om de wifi scanner te maken. Dit heb ik best zelfstandig kunnen oplossen. Voor een netwerkkaart in monitoring te zetten en terug in managed, heb ik een forum geraadpleegd en voor kennis over de kanalen van een frequentie de tabellen op Wikipedia. Daarnaast heb ik nog de documentatie van scapy gebruikt. Ik heb zeer veel geleerd en vond dit best interessant.

## Wifi scanner

Eerst wordt er vastgesteld dat de wifi kaart in managed staat om uit te weten te komen welke kanalen deze ondersteund. 
Dit zijn voornamelijk kanalen van 2.4GHz en 5GHz, maar moest iemand ook 6GHz kunnen gebruiken word hiervoor automatisch alle kanalen van gepakt met bijhorende frequentie. 

```
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = BASE_DIR + "/data"

INTERFACE = "wlp110s0"
INTERFACE_MON = f"{INTERFACE}mon"

try:
    network_to_managed(INTERFACE_MON)
except:
    print("Netwerk kaart staat al in managed.")
```

Hierna worden ook folders voorzien om alle data netjes te sorteren.

```
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)
    os.mkdir(f"{DATA_DIR}/2.4GHz")
    os.mkdir(f"{DATA_DIR}/5GHz")
    os.mkdir(f"{DATA_DIR}/6GHz")
```

Vervolgens wordt er een lijst gemaakt van alle bruikbare kanalen die de wifi kaart ondersteund.

```
stdout = Popen(f'iwlist {INTERFACE} channel', shell=True, stdout=PIPE).stdout
output = str(stdout.read()).replace(' ', '').split("\\n")
output.pop(0)
for i in range(3):
    output.pop(len(output)-1)

usable_channels = []
for out in output:
	split = out.split(":")
	usable_channels.append([int(split[0][7:]), float(split[1][:-3])])
```

Wanneer het python bestand gestart wordt, initialiseert al wat hierboven geplaatst is, wordt de `netwerk_sniffer` aangemaakt en de `main` fuctie gestart.

```
if __name__ == "__main__":
    try:
        netwerk_sniffer = AsyncSniffer(iface=INTERFACE_MON, prn=handle_packet)
        locky = threading.Lock()
        main()
    except KeyboardInterrupt:
        netwerk_sniffer.stop()
        network_to_managed(INTERFACE_MON)
```

De functie die de `netwerk_sniffer` gebruikt voor de packets is `handle_packet`, hierin wordt gekeken of de packet een *Beaconframe* is. Als dit correct is, worden alle gegevens van deze frame opgeslagen in een textbestand met het *ssid* als naam in de folder van het kanaal.

```
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
```

De `main` ziet er als volgt uit.

```
def main():
    network_to_monitor(INTERFACE)
    antwoord = ""
    while antwoord.lower() != "q":
        antwoord = input("(q)uit, (s)cannen: ")
        
        if antwoord.lower() == "s":
            seconden = input("Aantal seconden scannen per kanaal: ")
            
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
```

De bijhorende functies zijn in een ander bestand geplaatst en worden gebruikt om van kanaal te wisselen, de wifi kaart in monitoring te plaatsen en om de wifi kaart in managed te plaatsen.

```
def change_channel(interface_mon, channel):
    print(f'Channel: {channel}')
    Popen(f'iwconfig {interface_mon} channel {channel}', shell=True)

def network_to_monitor(interface):
    run("sudo airmon-ng check kill", shell=True)
    run(f"sudo airmon-ng start {interface}", shell=True)

def network_to_managed(interface_mon):
    run(f"sudo airmon-ng stop {interface_mon}", shell=True)
    run("sudo systemctl start NetworkManager", shell=True)
```