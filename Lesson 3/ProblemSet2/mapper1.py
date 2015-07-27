#!/usr/bin/python


import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, client, user, time, zone, method, path, protocol, status, size = data
		print path
