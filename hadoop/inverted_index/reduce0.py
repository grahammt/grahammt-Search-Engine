#!/usr/bin/env python3
"""Reduce 0."""
import sys

x = 0
for line in sys.stdin:
    sys.stdout.write(line.split("\t", 1)[1])
    x = x+1
f = open("total_document_count.txt", "w")
f.write(str(x))
