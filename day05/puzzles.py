# supplies are stored in buried crates
# giant cargo crane moves the crates
# move always those on top


# separate crates input from commands
# commands: get how many cranes to move, intial position, final destination
# turn columns of cranes into arrays/queues
# apply commands to crane queues

import io
import pandas as pd
from copy import deepcopy

INPUT_VALUES_FILE = 'input.txt'

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()

def get_last_characters(listname: list):
    return [letter[-1] for letter in listname]

# separate crates input from commands
input_crates, input_commands = read_file(INPUT_VALUES_FILE).split("\n\n")
commands = input_commands.split("\n")
crates = input_crates.replace("    ", "[ ] ").replace("]", "],").replace("   ", ",")

# commands: get how many cranes to move, intial position, final destination
commands_list = []
for command in commands:
    crate_from_to = [int(digit) for digit in command.split() if digit.isdigit()]
    commands_list.append(crate_from_to)

# turn columns of cranes into arrays/queues
df = pd.read_csv(io.StringIO(crates), sep=",", header=None)
df = df.fillna('')
head = df.tail(1)
header = [str(column).strip() for column in head.values[0]]# if column != '']
df.columns = header
df.drop(df.tail(1).index,inplace=True)
df.dropna(how='all', axis=1, inplace=True)

# turn columns of cranes into arrays/queues
crates_list = []
for column in df.columns:
    if column != '':        
        crate = [crate.replace("[", "").replace("]", "").strip() for crate in df[column].to_list() if crate.replace("[", "").replace("]", "").strip() != '']
        crate.reverse()
        crates_list.append(crate)

crates_list2 = deepcopy(crates_list)

# apply commands to crane queues
for index, command in enumerate(commands_list):
    crate_count, column_from, column_to = command
    pop_crates = [crates_list[column_from -1].pop() for idx in range(crate_count)]
    crates_list[column_to -1] += pop_crates
    # part two keep order
    slice_crates = crates_list2[column_from-1][-crate_count:]
    crates_list2[column_to -1] += slice_crates
    del crates_list2[column_from -1 ][-crate_count:]    


puzzle1_answer = ''.join(get_last_characters(crates_list))
puzzle2_answer = ''.join(get_last_characters(crates_list2))
print(puzzle1_answer)
print(puzzle2_answer)