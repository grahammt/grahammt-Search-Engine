#!/usr/bin/env python3
"""Map 3."""
import sys
import csv
import re
import json

words = {}

for line in sys.stdin:
    pairs = line.split("\t", 1)
    dic = json.loads(pairs[1])
    var=0

    docnorm = dic["docnorm"]
    words_in_doc = dic["words_in_doc"]
    for key, value in words_in_doc.items():
        if not key in words:
            words[key]={}
            words[key]["nk"]=value[1]
            words[key]["docs"] = {}
        words[key]["docs"][pairs[0]] = [value[0], docnorm]

for key, value in words.items():
    print(key + "\t" + json.dumps(value, separators=(',',':')))