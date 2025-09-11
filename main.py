import board
import consoleHandler

def runGame() -> None:
    """
    Run the Game
    """
    #main program loop
    programRunning: bool = True
    while programRunning == True:
        boardConfig: list[int] = board.initialBoard()
        player: int = 1
        movesMade: int = 0
        #main game loop
        gameRunning: bool = True
        while gameRunning == True:
            consoleHandler.startingMessage()
            consoleHandler.printBoard(boardConfig)

            #Get user input and change board
            inputPosition: int = consoleHandler.getPlayerInput(player, boardConfig)
            board.changeBoard(boardConfig, player, inputPosition)
            movesMade = movesMade + 1

            #change whos turn it is
            if(player == 1):
                player = 2
            else:
                player = 1

            win: int = board.winningCondition(boardConfig)

            if(win != 0):
                #end game loop and check if to end program loop
                gameRunning = False
                programRunning = consoleHandler.playerWon(win)
            elif(movesMade == 9):
                #end game loop and check if to end program loop
                gameRunning = False
                programRunning = consoleHandler.gameOver()

runGame()