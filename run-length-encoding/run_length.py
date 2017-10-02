from itertools import groupby
import re


def encode(sent):
    numbers_and_letters = [(str(len(list(group))), name) for name, group in groupby(sent)]
    not_nested_list = []

    for sublist in numbers_and_letters:
        for item in sublist:
            if item != '1':
                not_nested_list.append(item)

    return ''.join(not_nested_list)


def decode(code):
    numbers_and_letters = re.findall('(\d*)(\D{1})', code)
    list_of_letters = sum([int(length or 1) * [item] for length, item in numbers_and_letters], [])
    return ''.join(list_of_letters)
