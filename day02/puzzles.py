# Separate oponent and my own responses
# Make circular lists
# Assign values of rock, paper and scissor to letters
# calculate round plays

from enum import Enum

INPUT_VALUES_FILE = 'input.txt'
score = 0

class RoundPoints(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

class StrategyGuide2(Enum):
    WIN = 'X'
    DRAW = 'Y'
    LOSE = 'Z'

def read_file(filename: str):
    file = open(filename)
    try:
        return file.read()
    except Exception as e:
        print("Unable to open file {filename}. {exception}".format(filename = filename, exception=str(e)))
    finally:
        file.close()

def get_player_responses(input_list, player_response: 0 | 1):
    new_list = [response for response in input_list if input_list.index(response) % 2 % 2 == player_response]
    return new_list

def player_response_to_point(letter: str):
    if letter.upper() == 'A' or letter.upper() == 'X':
        return 1
    if letter.upper() == 'B' or letter.upper() == 'Y':
        return 2
    if letter.upper() == 'C' or letter.upper() == 'Z':
        return 3

def leftWins(player1, player2):
    check_list = [1, 2, 3]
    return player1 == player2 - 1 or (player1 == check_list[-1] and player2 == check_list[0])

responses_list = read_file(INPUT_VALUES_FILE).split()
ROUNDS = len(responses_list) // 2

# Separate oponent and my own responses in circular lists
oponent_response = get_player_responses(responses_list, 0)
own_response = get_player_responses(responses_list, 1)

# calculate round plays
for round in range(ROUNDS):
    oponent_move = player_response_to_point(oponent_response[round])
    own_move = player_response_to_point(own_response[round])
    if oponent_move == own_move:
        score += own_move + RoundPoints.DRAW.value
    if leftWins(oponent_move, own_move):
        score += own_move + RoundPoints.WIN.value
    if leftWins(own_move, oponent_move):
        score += own_move + RoundPoints.LOSE.value 


print("Score final: " + str(score))