# reads inputs
# split values in list of strings per line
# split each string on a half
# compare the strings to find the value in common
# calculate the priority
##  generate list of alphabet minuscule and maiuscule

import string
from itertools import islice

INPUT_VALUES_FILE = 'example-input.txt'
ALPHABET_LIST = list(string.ascii_letters)
puzzle1_priority = 0
puzzle2_priority = 0

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()

def spread_string_in_half(item: str):
    item_size = len(item)
    half = item_size//2
    first_half = set(item[:half])
    second_half = set(item[half:item_size])
    return first_half, second_half

def find_common_character_between(item1: set, item2: set):
    return list(item1.intersection(item2))[0]

def find_common_characters(item):
    print()

def convert_into_priority(character: str ):
    return ALPHABET_LIST.index(character) + 1

def chunk(element, size):
    it = iter(element)
    return list(iter(lambda: tuple(islice(it, size)), ()))

inputs = read_file(INPUT_VALUES_FILE).split()
groups_of_three_list = chunk(inputs,3)

for item in inputs:
    half_parts = spread_string_in_half(item)
    common_character = find_common_character_between(half_parts[0], half_parts[1])
    priority_value = convert_into_priority(common_character)    
    puzzle1_priority += priority_value       

for item in groups_of_three_list:
    common_value = list(set(item[0]) & set(item[1]) & set(item[2]))[0]
    puzzle2_priority += convert_into_priority(common_value)

print("Puzzle 1 - priority sum {total}".format(total=puzzle1_priority))
print("Puzzle 2 - priority sum {total}".format(total=puzzle2_priority))
