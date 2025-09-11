"""
Contains Logic for the Game Board
"""

def boardParser(number: int) -> str:
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
    
def changeBoard(boardConfig: list[int], type: int, position: int) -> None:
    """
    Edits the Board Config

    :param boardConfig: current board config
    :type boardConfig: list[int]
    :param type: What you want to write to the board
    :type type: int
    :param position: Position on the board you want to change
    """
    boardConfig[position] = type

def validConfig(boardConfig: list[int]) -> bool:
    """
    Check the validity of a board config based on:
    length and values

    :param boardConfig: The board config to be validated
    :type boardConfig: list[int]
    :return: If valid or not
    :rtype: bool
    """
    #check for correct length
    if(len(boardConfig) != 9):
        print("Board Config does not have the correct length of 9.")
        print(f"Given board length: {len(boardConfig)}")
        return False
    #check for invalid numbers in config
    for i in boardConfig:
        if(boardConfig[i] < 0 and boardConfig[i] > 2):
            print("Board Contains invalid numbers")
            print("Valid numbers: 0 for empty; 1 for x; 2 for o")
            print(f"Given number: {boardConfig[i]}")
            return False
    return True

def winningCondition(boardConfig: list[int]) -> int:
    """
    Checks any board config to see whether or not a player has Won
    Returns 0 for no win condition, 1 for x won and 2 for o won

    :param boardConfig: The board configuration to check
    :type boardConfig: list[int]
    :return: whether a player has won or not and which one
    :rtype: int
    """
    if(validConfig(boardConfig) == False):
        return 0
    #top row matches
    if(boardConfig[0] == boardConfig[1] == boardConfig[2] != 0):
        return boardConfig[0]
    #middle row matches
    if(boardConfig[3] == boardConfig[4] == boardConfig[5] != 0):
        return boardConfig[3]
    #bottom row matches
    if(boardConfig[6] == boardConfig[7] == boardConfig[8] != 0):
        return boardConfig[6]
    #left column matches
    if(boardConfig[0] == boardConfig[3] == boardConfig[6] != 0):
        return boardConfig[0]
    #middle column matches
    if(boardConfig[1] == boardConfig[4] == boardConfig[7] != 0):
        return boardConfig[1]
    #right column matches
    if(boardConfig[2] == boardConfig[5] == boardConfig[8] != 0):
        return boardConfig[2]
    #diagonal from top right matches
    if(boardConfig[0] == boardConfig[4] == boardConfig[8] != 0):
        return boardConfig[0]
    #diagonal from top left matches
    if(boardConfig[2] == boardConfig[4] == boardConfig[6] != 0):
        return boardConfig[2]
    return 0

#Converts player input (1a, 3b, C2...) to position in boardconfig list
#Returns -1 if input is invalid
def inputToBoardPosition(playerInput: str) -> int:
    """
    Converts player input (1a, 3b, C3, ...) to a position on the board
    Returns -1 if input is invalid

    :param playerInput: Any input string
    :type playerInput: str
    :return: Position on the board
    :rtype: int
    """
    #Top Left
    if(playerInput == "a1" or playerInput == "1a" or playerInput == "A1" or playerInput == "1A"):
        return 0
    #Top Middle
    if(playerInput == "b1" or playerInput == "1b" or playerInput == "B1" or playerInput == "1B"):
        return 1
    #Top Right
    if(playerInput == "c1" or playerInput == "1c" or playerInput == "C1" or playerInput == "1C"):
        return 2
    #Middle Left
    if(playerInput == "a2" or playerInput == "2a" or playerInput == "A2" or playerInput == "2A"):
        return 3
    #Middle Middle
    if(playerInput == "b2" or playerInput == "2b" or playerInput == "B2" or playerInput == "2B"):
        return 4
    #Middle Right
    if(playerInput == "c2" or playerInput == "2c" or playerInput == "C2" or playerInput == "2C"):
        return 5
    #Bottom Left
    if(playerInput == "a3" or playerInput == "3a" or playerInput == "A3" or playerInput == "3A"):
        return 6
    #Bottom Middle
    if(playerInput == "b3" or playerInput == "3b" or playerInput == "B3" or playerInput == "3B"):
        return 7
    #Bottom Right
    if(playerInput == "c3" or playerInput == "3c" or playerInput == "C3" or playerInput == "3C"):
        return 8
    return -1

def initialBoard() -> list[int]:
    """
    Generate an empty board

    :return: empty board config
    :rtype: list[int]
    """
    initialBoard: list[int] = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    return initialBoard