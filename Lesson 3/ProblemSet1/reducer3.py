#!/usr/bin/python

import sys

Number = 0
Value = 0

# Loop around the data
# It will be adding up number and value correspondingly

for line in sys.stdin:
    data_mapped = float(line.strip())

    Number += 1
    Value += data_mapped

print "{0}\t{1}".format(Number,Value)

