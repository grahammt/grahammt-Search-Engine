#!/usr/bin/env python3
import sys
import json
import math
import re
"""Map 2."""

documents={}
for line in sys.stdin:
    pairs = line.split("\t",1)
    tup=pairs[1].split(None,1)
    dic = json.loads(tup[1])
    nk = int(tup[0])
    for key, value in dic.items():
        if not key in documents:
            documents[key]={}
        documents[key][pairs[0]] = [value, nk]

for key, value in documents.items():
    print(key + "\t" + json.dumps(value,separators=(',',':'))) 
