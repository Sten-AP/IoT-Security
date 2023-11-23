from nmap import PortScanner
import json
import os


BASE_DIR = os.path.dirname(__file__)

nm = PortScanner()
nm.scan('localhost', '0-9000')


file = open(f"{BASE_DIR}/poortgegevens.json", "w")
hosts = []
for host in nm.all_hosts():
    host_data = {}
    host_data.update({"host": host})
    host_data.update({"name": nm[host].hostname()})
    host_data.update({"state": nm[host].state()})
    
    protocols = {}
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport = sorted(lport)
        
        ports = {}
        for port in lport:
            ports.update({port: nm[host][proto][port]['state']})
        protocols.update({proto: ports})
        
    host_data.update({"protocols": protocols})
    
    hosts.append(host_data)

hosts_json = json.dumps(hosts, indent=4)
file.write(str(hosts_json))
