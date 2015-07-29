#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader,None) #skip the header

for line in reader:
	if len(line) == 19:
		author_id = line[3]
		hour = int(line[8][11:13])
		print "{0}\t{1}".format(author_id, hour)
