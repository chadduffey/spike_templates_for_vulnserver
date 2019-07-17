from os import listdir
from os.path import isfile, join
import subprocess

files = [f for f in listdir('.') if isfile(join('.', f))]

target_ip = "10.0.0.99"
target_port = "9999"

for f in sorted(files):
	if ".spk" in f:
		print("Running: {}".format(f))	
		subprocess.call(["/usr/bin/generic_send_tcp", target_ip, target_port, f, "0", "0"])
