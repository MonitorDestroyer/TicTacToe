import board
import console_handler

def run_game() -> None:
    """
    Run the Game
    """
    #main program loop
    program_running: bool = True
    while program_running == True:
        board_config: list[int] = board.initial_board()
        player: int = 1
        moves_made: int = 0
        #main game loop
        game_running: bool = True
        while game_running == True:
            console_handler.starting_message()
            console_handler.print_board(board_config)

            #Get user input and change board
            input_position: int = console_handler.get_player_input(player, board_config)
            board.change_board(board_config, player, input_position)
            moves_made += 1

            #change whos turn it is
            if(player == 1):
                player = 2
            else:
                player = 1

            win: int = board.winning_condition(board_config)

            if(win != 0):
                #end game loop and check if to end program loop
                game_running = False
                program_running = console_handler.player_won(win)
            elif(moves_made == 9):
                #end game loop and check if to end program loop
                game_running = False
                program_running = console_handler.game_over()

run_game()