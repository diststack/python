#!/usr/bin/env python3

import sys
import re

def process_file(f):
    for line in f:
        if re.search(target, line):
            print(line, end = '')

if len(sys.argv)==1:
    print("usage: ")
    exit(1)

target = re.compile(sys.argv[1])
if len(sys.argv)==2:
    process_file(sys.stdin)
else: