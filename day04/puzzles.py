# generate lists from pair ranges
# count lists that are fully contained on another

INPUT_VALUES_FILE = 'input.txt'

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()

def generate_list_range(listname: list):
    start, stop = listname.split("-")
    return [i for i in range( int(start), int(stop) +1)]

def get_pair_list_range(listname: list):
    new_list = []
    for pair in listname:
        range1 = generate_list_range(pair[0])
        range2 = generate_list_range(pair[1])
        new_list.append([range1, range2])
    return new_list

def containsAll(lst1, lst2):
    return all([(x in lst2) for x in lst1])

def contains(lst1, lst2):
   return any([(x in lst2) for x in lst1])
  
input_list = read_file(INPUT_VALUES_FILE).split("\n")
range_pairs = [pair.split(",") for pair in input_list]
range_list = get_pair_list_range(range_pairs)
puzzle1_counter = 0
puzzle2_counter = 0
for pair in range_list:
    if containsAll(pair[0], pair[1]) or containsAll(pair[1], pair[0]):
        puzzle1_counter += 1
    if contains(pair[0], pair[1]) or contains(pair[1], pair[0]):
        puzzle2_counter += 1

print(puzzle1_counter)
print(puzzle2_counter)