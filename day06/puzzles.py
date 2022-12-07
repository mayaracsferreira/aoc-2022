# Look for groups of 4 non duplicated characters
# transform groups in set
# compare set size with list lenght
# count how many positions until the message begins 

INPUT_VALUES_FILE = 'input.txt'
MARKET_LENGTH_PUZZLE1 = 4
MARKET_LENGTH_PUZZLE2 = 14

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()

def find_packet_start_market(encrypt_msg, market_lenght):
    message_length = len(encrypt_msg)
    for index in range(message_length):
        if index > message_length - market_lenght:
            break
        start_signal_marker = encrypt_msg[index: index + market_lenght]
        if len(set(start_signal_marker)) == len(start_signal_marker):
            return(start_signal_marker, index + market_lenght)


input_signal = read_file(INPUT_VALUES_FILE).split("\n")
encrypted_signal = input_signal[0]

puzzle1_answer = find_packet_start_market(encrypted_signal, MARKET_LENGTH_PUZZLE1)
puzzle2_answer = find_packet_start_market(encrypted_signal, MARKET_LENGTH_PUZZLE2)

print("Puzzle 1: \nCharacters processed: {chars}.\nStart of message marker: {marker}".format(chars= puzzle1_answer[0], marker= puzzle1_answer[1]))
print("Puzzle 2: \nCharacters processed: {chars}.\nStart of message marker: {marker}".format(chars= puzzle2_answer[0], marker= puzzle2_answer[1]))