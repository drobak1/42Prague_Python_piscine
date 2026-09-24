#!/usr/bin/env py

def array_of_names(dic):
    arr = []
    for name, surname in dic.items():
         full_name = f"{name.capitalize()} {surname.capitalize()}"
         arr.append(full_name)
    return arr

people = {
     "jean": "valjean",
     "grace": "hopper",
     "xavier": "niel",
     "fifi": "brindacier"
}

print(array_of_names(people))