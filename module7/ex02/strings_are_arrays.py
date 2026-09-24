import sys
import re

params = sys.argv[1:]

if len(params) == 1:
    z = ""
    num_of_z = re.findall("z", params[0].lower())

    for i in num_of_z:
        z += "z"
    
    if len(z) > 0:
        print(z)
    else:
        print("none")
else: 
    print("none")

