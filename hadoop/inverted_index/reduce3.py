#!/usr/bin/env python3
"""Reduce 3."""
import sys
import json
import math
import re

docnorm = {}
nk = {}
total = open("total_document_count.txt", "r").read()
N = int(total)
out = {}
for line in sys.stdin:
    pairs = line.split("\t")
    dic = json.loads(pairs[1])
    if pairs[0] not in out:
        idf = math.log10(N/dic["nk"])
        out[pairs[0]] = ""
        nk[pairs[0]] = 0
    
    for key, value in dic["docs"].items():
        out[pairs[0]] += " " + str(key) + " " + str(value[0]) + " " + str(value[1])
        nk[pairs[0]]+=1

for key, value in out.items():
    idf = math.log10(N/nk[key])
    print(key + " " + str(idf) + value)
