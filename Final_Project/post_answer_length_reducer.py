#!/usr/bin/python

import sys

oldKey = None
question_length = 0
answer_length = 0
answer_amount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisKey, thisType, thisLength = data_mapped

    if oldKey and oldKey != thisKey:
        if answer_amount != 0:
            average_answer_length = answer_length / answer_amount
        else:
            average_answer_length = 0
        print "{0}\t{1}\t{2}".format(oldKey, question_length, average_answer_length)
        oldKey = thisKey
    answer_length = 0
    answer_amount = 0
    question_length = 0

    oldKey = thisKey
    if thisType == "question":
    question_length = int(thisLength)
    if thisType == "answer":
    answer_length += float(thisLength)
        answer_amount += 1

if oldKey != None:
    if answer_amount != 0:
    average_answer_length = answer_length / answer_amount
    print "{0}\t{1}\t{2}".format(oldKey, question_length, average_answer_length)
    else:
        print "{0}\t{1}\t{2}".format(oldKey, question_length, 0)