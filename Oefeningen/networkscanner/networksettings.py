from subprocess import Popen, run


def change_channel(interface_mon, channel):
    print(f'Channel: {channel}')
    Popen(f'iwconfig {interface_mon} channel {channel}', shell=True)

def network_to_monitor(interface):
    run("sudo airmon-ng check kill", shell=True)
    run(f"sudo airmon-ng start {interface}", shell=True)

def network_to_managed(interface_mon):
    run(f"sudo airmon-ng stop {interface_mon}", shell=True)
    run("sudo systemctl start NetworkManager", shell=True)