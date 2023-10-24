from subprocess import PIPE, Popen

interface = "wlp110s0"

stdout = Popen('iwlist ' + interface + ' channel', shell=True, stdout=PIPE).stdout
output = str(stdout.read()).replace(' ', '').split("\\n")
output.pop(0)
for i in range(3):
    output.pop(len(output)-1)

usable_channels = []
for out in output:
	split = out.split(":")
	usable_channels.append({int(split[0][7:]): float(split[1][:-3])})