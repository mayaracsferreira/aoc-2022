# reads inputs
# split values in list of strings per line
# split each string on a half
# compare the strings to find the value in common
# calculate the priority
##  generate list of alphabet minuscule and maiuscule

import string

INPUT_VALUES_FILE = 'input.txt'
ALPHABET_LIST = list(string.ascii_letters)
priority_sum = 0

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()

inputs = read_file(INPUT_VALUES_FILE).split()
print(ALPHABET_LIST)
for item in inputs:
    item_size = len(item)
    half = item_size//2
    first_half = set(item[:half])
    second_half = set(item[half:item_size])
    common_character = list(first_half.intersection(second_half))[0]
    priority_value = ALPHABET_LIST.index(common_character) + 1
    priority_sum += priority_value    
    print("Original string: {original}".format(original=item))
    #print("First half {first_half}".format(first_half=first_half))
    #print("Second half {second_half}".format(second_half=second_half))
    print("Common value between two strings {common_character}".format(common_character=common_character))
    print("Priority {priority}".format(priority=priority_value))
    print()

print(inputs)
print("Priority sum {total}".format(total=priority_sum))