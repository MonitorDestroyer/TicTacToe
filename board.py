"""
Contains Logic for the Game Board
"""

def board_parser(number: int) -> str:
    """
    Get the character associated with a number in the board config
    
    :param number: Associated number
    :type number: int
    :return: Character the number represents
    :rtype: str
    """
    if(number == 0):
        return ' '
    elif(number == 1):
        return 'x'
    elif(number == 2):
        return 'o'
    else:
        return '?'
    
def change_board(board_config: list[int], type: int, position: int) -> None:
    """
    Edits the Board Config

    :param board_config: current board config
    :type board_config: list[int]
    :param type: What you want to write to the board
    :type type: int
    :param position: Position on the board you want to change
    """
    board_config[position] = type

def valid_config(board_config: list[int]) -> bool:
    """
    Check the validity of a board config based on:
    length and values

    :param board_config: The board config to be validated
    :type board_config: list[int]
    :return: If valid or not
    :rtype: bool
    """
    #check for correct length
    if(len(board_config) != 9):
        print("Board Config does not have the correct length of 9.")
        print(f"Given board length: {len(board_config)}")
        return False
    #check for invalid numbers in config
    for i in board_config:
        if(board_config[i] < 0 and board_config[i] > 2):
            print("Board Contains invalid numbers")
            print("Valid numbers: 0 for empty; 1 for x; 2 for o")
            print(f"Given number: {board_config[i]}")
            return False
    return True

def winning_condition(board_config: list[int]) -> int:
    """
    Checks any board config to see whether or not a player has Won
    Returns 0 for no win condition, 1 for x won and 2 for o won

    :param board_config: The board configuration to check
    :type board_config: list[int]
    :return: whether a player has won or not and which one
    :rtype: int
    """
    if(valid_config(board_config) == False):
        return 0
    #top row matches
    if(board_config[0] == board_config[1] == board_config[2] != 0):
        return board_config[0]
    #middle row matches
    if(board_config[3] == board_config[4] == board_config[5] != 0):
        return board_config[3]
    #bottom row matches
    if(board_config[6] == board_config[7] == board_config[8] != 0):
        return board_config[6]
    #left column matches
    if(board_config[0] == board_config[3] == board_config[6] != 0):
        return board_config[0]
    #middle column matches
    if(board_config[1] == board_config[4] == board_config[7] != 0):
        return board_config[1]
    #right column matches
    if(board_config[2] == board_config[5] == board_config[8] != 0):
        return board_config[2]
    #diagonal from top right matches
    if(board_config[0] == board_config[4] == board_config[8] != 0):
        return board_config[0]
    #diagonal from top left matches
    if(board_config[2] == board_config[4] == board_config[6] != 0):
        return board_config[2]
    return 0

#Converts player input (1a, 3b, C2...) to position in boardconfig list
#Returns -1 if input is invalid
def input_to_board_position(player_input: str) -> int:
    """
    Converts player input (1a, 3b, C3, ...) to a position on the board
    Returns -1 if input is invalid

    :param player_input: Any input string
    :type player_input: str
    :return: Position on the board
    :rtype: int
    """
    #Top Left
    if(player_input == "a1" or player_input == "1a" or player_input == "A1" or player_input == "1A"):
        return 0
    #Top Middle
    if(player_input == "b1" or player_input == "1b" or player_input == "B1" or player_input == "1B"):
        return 1
    #Top Right
    if(player_input == "c1" or player_input == "1c" or player_input == "C1" or player_input == "1C"):
        return 2
    #Middle Left
    if(player_input == "a2" or player_input == "2a" or player_input == "A2" or player_input == "2A"):
        return 3
    #Middle Middle
    if(player_input == "b2" or player_input == "2b" or player_input == "B2" or player_input == "2B"):
        return 4
    #Middle Right
    if(player_input == "c2" or player_input == "2c" or player_input == "C2" or player_input == "2C"):
        return 5
    #Bottom Left
    if(player_input == "a3" or player_input == "3a" or player_input == "A3" or player_input == "3A"):
        return 6
    #Bottom Middle
    if(player_input == "b3" or player_input == "3b" or player_input == "B3" or player_input == "3B"):
        return 7
    #Bottom Right
    if(player_input == "c3" or player_input == "3c" or player_input == "C3" or player_input == "3C"):
        return 8
    return -1

def initial_board() -> list[int]:
    """
    Generate an empty board

    :return: empty board config
    :rtype: list[int]
    """
    initial_board: list[int] = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    return initial_board