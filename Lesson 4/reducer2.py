#!/usr/bin/python

import sys
from datetime import datetime

count = 0
sales = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", sales/count
        oldKey = thisKey;
        count = 0
    sales = 0

    oldKey = thisKey
    count += 1
    sales += float(thisSale)

if oldKey != None:
    print oldKey, "\t", sales/count

