import sys, re

params = sys.argv[1:]

if len(params) > 0:
    for param in params:
        if param.find("ism") == -1:
            print(param + "ism")
else:
    print("none")

