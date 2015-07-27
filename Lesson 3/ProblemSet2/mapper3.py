#!/usr/bin/python


import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		ip, client, user, time, zone, method, path, protocol, status, size = data
		if path.find("http://www.the-associates.co.uk") != -1:
			path = path.replace("http://www.the-associates.co.uk", "")
		print path
