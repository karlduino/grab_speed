#!/bin/bash

date +"%a %d %h %Y %r" >> /home/pi/nagios_data/speed.txt
grep Download /usr/local/nagios/var/status.dat >> /home/pi/nagios_data/speed.txt
