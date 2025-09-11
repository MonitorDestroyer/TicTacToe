"""
Handles Console In-/Output
"""

import board

def printBoard(boardConfig: list[int]) -> None:
   """
   Print Board to the console, based on any configuration

   :param boardConfig: the board configuration you want to be printed
   :type boardConfig: list[int]
   """
   if(board.validConfig(boardConfig) == False):
      print("Invalid board Configuration")
      return
   print("  a b c")
   print(f"1|{board.boardParser(boardConfig[0])}|{board.boardParser(boardConfig[1])}|{board.boardParser(boardConfig[2])}|")
   print(f"2|{board.boardParser(boardConfig[3])}|{board.boardParser(boardConfig[4])}|{board.boardParser(boardConfig[5])}|")
   print(f"3|{board.boardParser(boardConfig[6])}|{board.boardParser(boardConfig[7])}|{board.boardParser(boardConfig[8])}|")

def getPlayerInput(player: int, boardConfig: list[int]) -> int:
   """
   Get Player input validates it and returns position in boardconfig list
   Returns -1 on failure to assign

   :param player: The id of the player(1 for x and 2 for o)
   :type player: int
   :param boardConfig: The current board config
   :type boardConfig: list[int]
   :return: The position the player chose
   :rtype: int
   """
   incorrect: bool = True
   playerCharacter: str = board.boardParser(player)
   #set default return to -1
   inputConverted: int = -1
   while incorrect == True:
      print(f"Player {playerCharacter.upper()}, please enter where you would like to add your {playerCharacter}.")
      print("(Format: 1a, b3, 2A, C2)")
      #get player input and convert it to board position
      playerInput: str = input("Position: ")
      inputConverted = board.inputToBoardPosition(playerInput)
      #check if player input is a valid position
      if(inputConverted != -1):
      #Check if the selected position is empty
         if(boardConfig[inputConverted] == 0):
            incorrect = False
         else:
            print("The position you select must be empty")
      else:
         print("Invalid input, please try again.")
   return inputConverted

def startingMessage() -> None:
    """
    Print the welcome message
    """
    print("============================================")
    print("Welcome to the wonderful game of Tic Tac Toe")
    print("============================================")

def playerWon(player: int) -> bool:
   """
   Win Message, also asks if players want to play again

   :param player: player id
   :type player: int
   :return: Whether to play again or not
   :rtype: bool
   """
   playerCharacter: str = board.boardParser(player)
   print(f"Congratulations Player {playerCharacter.upper()}, you won!")
   print("If you would like a rematch, please enter 'again'")
   againInput: str = input("Rematch?: ")
   if(againInput == "again"):
      return True
   print("Goodbye")
   return False

def gameOver() -> bool:
   """"
   Game over Message when no more moves are available
   also asks player whether to play again or not

   :return: Whether to play again or not
   :rtype: bool
   """
   print("It's a draw, there are no more possible moves to make")
   print("If you would like a rematch, please enter 'again'")
   againInput: str = input("Rematch?: ")
   if(againInput == "again"):
      return True
   print("Goodbye")
   return False