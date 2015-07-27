#!/usr/bin/python

import sys

highestSales = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then only the highest sales will be returned for individual store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSales
        oldKey = thisKey;
        highestSales = 0
    else:
        if float(thisSale) > highestSales:
            highestSales = float(thisSale)
        
    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", highestSales

