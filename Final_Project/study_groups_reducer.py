#!/usr/bin/python

import sys

oldKey = None
users = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisUser = data_mapped

    if oldKey and oldKey != thisKey:
    print "{0}\t{1}".format(oldKey, users)
        oldKey = thisKey
    users = []

    oldKey = thisKey
    users.append(int(thisUser))

if oldKey != None:
    print "{0}\t{1}".format(oldKey, users)




