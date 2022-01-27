#!/usr/bin/env python3
"""Map 1."""

import sys
import csv
import re
import logging
import json

csv.field_size_limit(sys.maxsize)

words = {}
#print("yesss")
stopWordz = open("stopwords.txt", "r").read().split("\n")

for row in csv.reader(sys.stdin):
    row[1] = row[1].lower()
    row[2] = row[2].lower()

    fullLine = row[1].split()
    fullLine.extend(row[2].split())
    
    for x in fullLine:
        word = re.sub(r'[^a-zA-Z0-9]+', '', x)
        if word and word not in stopWordz:
            if word in words:
                if row[0] in words[word]:
                    words[word][row[0]] += 1
                else:
                    words[word][row[0]] = 1
            else:
                words[word] = {}
                words[word][row[0]] = 1

            
for key, value in words.items():
    print(str(key) + "\t" + json.dumps(value, separators=(',', ':')))
