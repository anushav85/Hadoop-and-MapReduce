#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader,None) #skip the header

for line in reader:
    if len(line) == 19:
        tagnames = line[2]
        node_id = line[0]
        node_type = line[5]
        if node_type == "question":
            print "{0}\t{1}".format(node_id, tagnames)
