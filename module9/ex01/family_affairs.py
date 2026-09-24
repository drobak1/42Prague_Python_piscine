#!/usr/bin/env py


def find_the_redheads(dic):

    def is_redhead(name):
        return dic[name] == "red"

    redheads = filter(is_redhead, dic.keys())
    return list(redheads)

dupont_family = {
    "dan": "red",
    "jana": "blond",
    "david": "red",
    "jan": "brunette",
    "michal": "red"
}

print(find_the_redheads(dupont_family))