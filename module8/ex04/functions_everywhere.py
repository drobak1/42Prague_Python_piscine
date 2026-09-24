#!/usr/bin/env py

import sys

def shrink(str):
    print(str[0:8])

def enlarge(str):
    while len(str) < 8:
        str += "Z"
    print(str)

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        if len(param) > 8:
            shrink(param)
        elif len(param) == 0:
            print(param)
        else:
            enlarge(param)
else:
    print("none")