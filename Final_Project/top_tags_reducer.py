#!/usr/bin/python

import sys

tags = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    node_id, tagnames = data_mapped
    #list of tags are space separated

    for tagname in tagnames.strip().split():
        if tagname in tags:
            tags[tagname] += 1
        else:
            tags[tagname] = 1

sortedtags = sorted(tags, key=tags.get, reverse=True)
top10tags = sortedtags[:10]

for tagname in top10tags:
    print "{0}\t{1}".format(tagname, tags[tagname])

# Another sort method:
# sortedtags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
# top10tags = sortedtags[:10]

# for tag in top10tags:
#     print "{0}\t{1}".format(tag[0], tag[1])


