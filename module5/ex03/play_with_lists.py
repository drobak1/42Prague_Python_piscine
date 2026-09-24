my_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set({})

for num in my_list:
    if num > 5:
        new_set.add(num + 2)

print(my_list)
print(new_set)