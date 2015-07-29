#!/usr/bin/python

import sys

oldKey = None
posted_hours = {}

for i in range(24):
    posted_hours[i] = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, hournow = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", max(posted_hours, key=posted_hours.get)
        oldKey = thisKey
        for i in range(24):
            posted_hours[i] = 0

    oldKey = thisKey
    posted_hours[int(hournow)] += 1

if oldKey != None:
    print oldKey, "\t", max(posted_hours, key=posted_hours.get)