#!/usr/bin/env python3
# grab speed from nagios data file
# us

import os
import subprocess

primary_nagios_file = '/usr/local/nagios/var/status.dat'
speed_file = '/home/pi/nagios_data/speed.txt'
tmp_file = '/tmp/this_speed.txt'
max_char = 140

# grep to pull out the results
with open(os.devnull, 'w') as DEVNULL:
    command = ['grep', 'Download', primary_nagios_file]
    subprocess.call(command, stdout=open(tmp_file, 'w'), stderr=DEVNULL)

# determine the number of charaters in the tmp file
fin = open(tmp_file, 'r')
result = "".join(fin.readlines())
fin.close()

if len(result) < max_char:
    with open(os.devnull, 'w') as DEVNULL:
        fp = open(speed_file, 'a')
        fp.write(result)
        subprocess.call('date', stdout=fp, stderr=DEVNULL)
        fp.close()
