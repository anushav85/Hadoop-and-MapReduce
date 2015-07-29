#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    words = re.split(r'.,!?:;"()<>{}#$=-/', line[4])
    for word in words:
        if(len(word) > 1):
            print "{0}\t{1}".format(word.strip().lower(), line[0])
