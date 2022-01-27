#!/usr/bin/env python3
"""Reduce 1."""
import sys
import json
import math
import re

out = {}

i = open("total_document_count.txt", "r").read()
N = int(i)
for line in sys.stdin:
    pairs = line.split("\t")
    dic = json.loads(pairs[1])
    if pairs[0] not in out:
        out[pairs[0]] = {}
        out[pairs[0]]["nk"] = len(dic)
        out[pairs[0]]["tmp"] = dic
    else:
        out[pairs[0]]["nk"] += len(dic)
        out[pairs[0]]["tmp"].update(dic)
    
for key, value in out.items():    
    print(key+"\t"+str(value["nk"]) + " "  + json.dumps(value["tmp"], separators=(',', ':')))
