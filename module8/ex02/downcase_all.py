import sys


def downcase_it(str: str) -> str:
    return str.lower()

params = sys.argv[1:]

for param in params:
    print(downcase_it(param))
