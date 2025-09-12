"""
Handles Console In-/Output
"""

import board

def print_board(board_config: list[int]) -> None:
   """
   Print Board to the console, based on any configuration

   :param board_config: the board configuration you want to be printed
   :type board_config: list[int]
   """
   if(board.valid_config(board_config) == False):
      print("Invalid board Configuration")
      return
   print("  a b c")
   print(f"1|{board.board_parser(board_config[0])}|{board.board_parser(board_config[1])}|{board.board_parser(board_config[2])}|")
   print(f"2|{board.board_parser(board_config[3])}|{board.board_parser(board_config[4])}|{board.board_parser(board_config[5])}|")
   print(f"3|{board.board_parser(board_config[6])}|{board.board_parser(board_config[7])}|{board.board_parser(board_config[8])}|")

def get_player_input(player: int, board_config: list[int]) -> int:
   """
   Get Player input validates it and returns position in boardconfig list
   Returns -1 on failure to assign

   :param player: The id of the player(1 for x and 2 for o)
   :type player: int
   :param board_config: The current board config
   :type board_config: list[int]
   :return: The position the player chose
   :rtype: int
   """
   incorrect: bool = True
   player_character: str = board.board_parser(player)
   #set default return to -1
   input_converted: int = -1
   while incorrect == True:
      print(f"Player {player_character.upper()}, please enter where you would like to add your {player_character}.")
      print("(Format: 1a, b3, 2A, C2)")
      #get player input and convert it to board position
      player_input: str = input("Position: ")
      input_converted = board.input_to_board_position(player_input)
      #check if player input is a valid position
      if(input_converted != -1):
      #Check if the selected position is empty
         if(board_config[input_converted] == 0):
            incorrect = False
         else:
            print("The position you select must be empty")
      else:
         print("Invalid input, please try again.")
   return input_converted

def starting_message() -> None:
    """
    Print the welcome message
    """
    print("============================================")
    print("Welcome to the wonderful game of Tic Tac Toe")
    print("============================================")

def player_won(player: int) -> bool:
   """
   Win Message, also asks if players want to play again

   :param player: player id
   :type player: int
   :return: Whether to play again or not
   :rtype: bool
   """
   player_character: str = board.board_parser(player)
   print(f"Congratulations Player {player_character.upper()}, you won!")
   print("If you would like a rematch, please enter 'again'")
   again_input: str = input("Rematch?: ")
   if(again_input == "again"):
      return True
   print("Goodbye")
   return False

def game_over() -> bool:
   """"
   Game over Message when no more moves are available
   also asks player whether to play again or not

   :return: Whether to play again or not
   :rtype: bool
   """
   print("It's a draw, there are no more possible moves to make")
   print("If you would like a rematch, please enter 'again'")
   again_input: str = input("Rematch?: ")
   if(again_input == "again"):
      return True
   print("Goodbye")
   return False