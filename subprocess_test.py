#!/usr/bin/env python3
from subprocess import Popen, PIPE

lister = Popen(['ls','-l'], stdout=PIPE)

for bytes in lister.stdout:
    line = bytes.decode()
    if line.startswith('total'):
        continue
    spiltline = line.split()
    if int(spiltline[4]) > 1000:
        print(spiltline[8], spiltline[4])
# p = subprocess.Popen(['ls -l /etc/p*', shell=True])