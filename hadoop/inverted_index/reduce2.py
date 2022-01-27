#!/usr/bin/env python3
"""Reduce 2."""

import sys
import json
import math
import re

total = open("total_document_count.txt", "r").read()
N = int(total)
docnorm = {}
for line in sys.stdin:
    pairs = line.split("\t")
    dic = json.loads(pairs[1])
    for key, value in dic.items():
        if pairs[0] not in docnorm:
            docnorm[pairs[0]] = {}
            docnorm[pairs[0]]["docnorm"] = value[0] ** 2 * math.log10(N/value[1])**2
            docnorm[pairs[0]]["dic"] = dic
        else:
            docnorm[pairs[0]]["docnorm"] += value[0] ** 2 * math.log10(N/value[1])**2
            docnorm[pairs[0]]["dic"].update(dic)
for key, value in docnorm.items():
    print(key+"\t" + json.dumps({"docnorm": value["docnorm"], "words_in_doc": value["dic"]}, separators=(',', ':')))
