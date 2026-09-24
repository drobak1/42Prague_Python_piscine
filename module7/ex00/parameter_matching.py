import sys


if len(sys.argv) - 1 == 1:
    key_word = str(sys.argv[1])
    text = str(input("What was the parameter? "))
    if key_word == text:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")

