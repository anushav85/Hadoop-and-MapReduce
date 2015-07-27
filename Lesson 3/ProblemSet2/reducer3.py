#!/usr/bin/python

import sys

oldKey = None
url_count = 0
most_popular_url = ''
most_popular_url_count = 0

for line in sys.stdin:
    data_mapped = line.strip()

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        if url_count > most_popular_url_count:
            most_popular_url_count = url_count
            most_popular_url = oldKey
        oldKey = thisKey;
        url_count = 0

    oldKey = thisKey
    url_count += 1

if url_count > most_popular_url_count:
    most_popular_url = oldKey
    most_popular_url_count = url_count

if most_popular_url != None:
    print most_popular_url, "\t", most_popular_url_count

