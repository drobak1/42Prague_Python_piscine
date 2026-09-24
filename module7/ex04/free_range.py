import sys

numbers = sys.argv[1:]
arr = []

if len(numbers) == 2 and int(numbers[0]) < int(numbers[1]):
    for i in range(int(numbers[0]),int(numbers[1]) + 1):
        arr.append(i)
    print(arr)
else:
    print("none")