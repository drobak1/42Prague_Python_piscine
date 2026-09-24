import sys

parmas = sys.argv[1:]

if len(parmas) > 0:
    print(f"Parameters: {len(parmas)}")
    for param in parmas:
        print(f"{param}: {len(param)}")
else:
    print("none")