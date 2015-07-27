#!/usr/bin/python

import sys

oldKey = None
Count = 0

for line in sys.stdin:
    data_mapped = line.strip()

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", Count
        oldKey = thisKey;
        Count = 0

    oldKey = thisKey
    Count += 1

if oldKey != None:
    print oldKey, "\t", Count

