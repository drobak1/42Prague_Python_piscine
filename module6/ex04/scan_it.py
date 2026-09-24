import re
import sys



if len(sys.argv) == 3:
    key_word = sys.argv[1]
    text = sys.argv[2]
    matches = re.findall(key_word, text)
    if len(matches) != 0:
        print(len(matches))
    else:
        print("none")
else:
    print("none")

