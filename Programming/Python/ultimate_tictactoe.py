

player = "X"
playableRows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playableCols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
overallx = ["$", "$", "$", "$", "$", "$", "$", "$", "$"]
overallo = ["$", "$", "$", "$", "$", "$", "$", "$", "$"]
cellDict ={
    1: [[0,1,2], [0,2,4]],
    2: [[0,1,2], [6,8,10]],
    3: [[0,1,2], [12,14,16]],
    4: [[3,4,5], [0,2,4]],
    5: [[3,4,5], [6,8,10]],
    6: [[3,4,5], [12,14,16]],
    7: [[6,7,8], [0,2,4]],
    8: [[6,7,8], [6,8,10]],
    9: [[6,7,8], [12,14,16]]
}

prohibitedRCs = []
gameActive = True
board = [
    ['_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_'],
    ['_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_'],
    [' ', '|', ' ', '|', ' ', ' || ',' ', '|', ' ', '|', ' ', ' || ',' ', '|', ' ', '|', ' ', '\n======================='],
    ['_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_'],
    ['_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_'],
    [' ', '|', ' ', '|', ' ', ' || ',' ', '|', ' ', '|', ' ', ' || ',' ', '|', ' ', '|', ' ', '\n======================='],
    ['_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_'],
    ['_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_', ' || ','_', '|', '_', '|', '_'],
    [' ', '|', ' ', '|', ' ', ' || ',' ', '|', ' ', '|', ' ', ' || ',' ', '|', ' ', '|', ' ']
]

def drawBoard():
    global board
    for row in board:
        for col in row:
            print(col, end='')
        print()

def oneTurn():
    global board
    global player
    global playableRows
    global playableCols
    global prohibitedRCs
    global overallx
    global overallo
    global gameActive
    print(f'It is currently {player}\'s turn.')
    print(f'The playabe rows are {playableRows} and the playable columns are {playableCols}.')
    moveRow = int(input("Please enter row you would like to play on: "))
    moveCol = int(input("Please enter the column you would like to play on: "))
    if moveRow in playableRows and moveCol in playableCols:
        if (board[moveRow - 1][(moveCol - 1) * 2] == " " or board[moveRow - 1][(moveCol - 1) * 2] == "_") and ((moveRow - 1, (moveCol - 1) * 2)) not in prohibitedRCs:
            board[moveRow - 1][(moveCol - 1) * 2] = player
            if player == "X":
                player = "O"
            else:
                player ="X"
            if (moveRow - 1, (moveCol - 1) * 2) in prohibitedRCs:
                playableRows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            elif moveRow in [1, 4, 7]:
                playableRows = [1, 2, 3]
            elif moveRow in [2, 5, 8]:
                playableRows = [4, 5, 6]
            elif moveRow in [3, 6, 9]:
                playableRows = [7, 8, 9]
            if (moveRow - 1, (moveCol - 1) * 2) in prohibitedRCs:
                playableCols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            elif moveCol in [1, 4, 7]:
                playableCols = [1, 2, 3]
            elif moveCol in [2, 5, 8]:
                playableCols = [4, 5, 6]
            elif moveCol in [3, 6, 9]:
                playableCols = [7, 8, 9]
            cellWinCondition()
            if (playableRows[0] - 1, (playableCols[0] - 1) * 2) in prohibitedRCs:
                playableRows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                playableCols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if winConX(overallx) == True:
                gameActive = False
                drawBoard()
                print("X won the game!")
            elif winConO(overallo) == True:
                gameActive = False
                drawBoard()
                print("O won the game!")
        else:
            print("Invalid move!")
    else:
        print("Invalid move!")    

def cellWinCondition():
    '''
    Basically we have the boards like this:
    (0-2, {0, 2, 4}) (0-2, {6, 8, 10}) (0-2, {12, 14, 16})
    (3-5, {0, 2, 4}) (3-5, {6, 8, 10}) (3-5, {12, 14, 16})
    (6-8, {0, 2, 4}) (6-8, {6, 8, 10}) (6-8, {12, 14, 16})
    where each intersection of the x and y values in a tuple is a location in our list that is playable and in that subboard
    so win-conditions look like:
    YO WHAT IF I CREATE A NEW LIST THAT JUST SAMPLES THE BOARD AND THEN CHECK PATTERNS IN THAT LIST!!
    so win-condition like that is(# is placeholder): 
    X##X##X##
    #X##X##X#
    ##X##X##X
    XXX######
    ###XXX###
    ######XXX
    X###X###X
    ##X#X#X##
    and the same for O's:
    O##O##O##
    #O##O##O#
    ##O##O##O
    OOO######
    ###OOO###
    ######OOO
    O###O###O
    ##O#O#O##

    '''
    sample1 = [board[0][0], board[0][2], board[0][4], board[1][0], board[1][2], board[1][4], board[2][0], board[2][2], board[2][4]]
    sample2 = [board[0][6], board[0][8], board[0][10], board[1][6], board[1][8], board[1][10], board[2][6], board[2][8], board[2][10]]
    sample3 = [board[0][12], board[0][14], board[0][16], board[1][12], board[1][14], board[1][16], board[2][12], board[2][14], board[2][16]]
    sample4 = [board[3][0], board[3][2], board[3][4], board[4][0], board[4][2], board[4][4], board[5][0], board[5][2], board[5][4]]
    sample5 = [board[3][6], board[3][8], board[3][10], board[4][6], board[4][8], board[4][10], board[5][6], board[5][8], board[5][10]]
    sample6 = [board[3][12], board[3][14], board[3][16], board[4][12], board[4][14], board[4][16], board[5][12], board[5][14], board[5][16]]
    sample7 = [board[6][0], board[6][2], board[6][4], board[7][0], board[7][2], board[7][4], board[8][0], board[8][2], board[8][4]]
    sample8 = [board[6][6], board[6][8], board[6][10], board[7][6], board[7][8], board[7][10], board[8][6], board[8][8], board[8][10]]
    sample9 = [board[6][12], board[6][14], board[6][16], board[7][12], board[7][14], board[7][16], board[8][12], board[8][14], board[8][16]]
    samples = [sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8, sample9]
    cell = 0
    for sample in samples:
        cell += 1
        if winConX(sample) == True:
            scoreX(cell)
            prohibitedRanges(cell)
            #samples[cell-1] = "Done"
        elif winConO(sample) == True:
            scoreO(cell)
            prohibitedRanges(cell)
            #samples[cell-1] = "Done"

def winConX(sample):
    #sample is input as a 1d list of the board condition
    if sample == "Done":
        return False
    else:
        if sample[0] == 'X' and sample[3] == 'X' and sample[6] == 'X':
            return  True
        elif sample[1] == 'X' and sample[4] == 'X' and sample[7] == 'X':
            return True
        elif sample[2] == 'X' and sample[5] == 'X' and sample[8] == 'X':
            return True
        elif sample[0] == 'X' and sample[1] == 'X' and sample[2] == 'X':
            return True
        elif sample[3] == 'X' and sample[4] == 'X' and sample[5] == 'X':
            return True
        elif sample[6] == 'X' and sample[7] == 'X' and sample[8] == 'X':
            return True
        elif sample[0] == 'X' and sample[4] == 'X' and sample[8] == 'X':
            return True
        elif sample[2] == 'X' and sample[4] == 'X' and sample[6] == 'X':
            return True
        else:
            return False

def winConO(sample):
    #sample is input as a 1d list of the board condition
    if sample == "Done":
        return False
    else:
        if sample[0] == 'O' and sample[3] == 'O' and sample[6] == 'O':
            return  True
        elif sample[1] == 'O' and sample[4] == 'O' and sample[7] == 'O':
            return True
        elif sample[2] == 'O' and sample[5] == 'O' and sample[8] == 'O':
            return True
        elif sample[0] == 'O' and sample[1] == 'O' and sample[2] == 'O':
            return True
        elif sample[3] == 'O' and sample[4] == 'O' and sample[5] == 'O':
            return True
        elif sample[6] == 'O' and sample[7] == 'O' and sample[8] == 'O':
            return True
        elif sample[0] == 'O' and sample[4] == 'O' and sample[8] == 'O':
            return True
        elif sample[2] == 'O' and sample[4] == 'O' and sample[6] == 'O':
            return True
        else:
            return False

def scoreX(cell):
    global overallx
    overallx[cell - 1] = "X"
    if cell == 1:
        board[0][0] = " "
        board[0][1] = " "
        board[0][2] = " "
        board[0][3] = " "
        board[0][4] = " "
        board[1][0] = " "
        board[1][1] = " "
        board[1][2] = "X"
        board[1][3] = " "
        board[1][4] = " "
        board[2][0] = " "
        board[2][1] = " "
        board[2][2] = " "
        board[2][3] = " "
        board[2][4] = " "
    elif cell == 2:
        board[0][6] = " "
        board[0][7] = " "
        board[0][8] = " "
        board[0][9] = " "
        board[0][10] = " "
        board[1][6] = " "
        board[1][7] = " "
        board[1][8] = "X"
        board[1][9] = " "
        board[1][10] = " "
        board[2][6] = " "
        board[2][7] = " "
        board[2][8] = " "
        board[2][9] = " "
        board[2][10] = " "
    elif cell == 3:
        board[0][12] = " "
        board[0][13] = " "
        board[0][14] = " "
        board[0][15] = " "
        board[0][16] = " "
        board[1][12] = " "
        board[1][13] = " "
        board[1][14] = "X"
        board[1][15] = " "
        board[1][16] = " "
        board[2][12] = " "
        board[2][13] = " "
        board[2][14] = " "
        board[2][15] = " "
        board[2][16] = " "
    elif cell == 4:
        board[3][0] = " "
        board[3][1] = " "
        board[3][2] = " "
        board[3][3] = " "
        board[3][4] = " "
        board[4][0] = " "
        board[4][1] = " "
        board[4][2] = "X"
        board[4][3] = " "
        board[4][4] = " "
        board[5][0] = " "
        board[5][1] = " "
        board[5][2] = " "
        board[5][3] = " "
        board[5][4] = " "
    elif cell == 5:
        board[3][6] = " "
        board[3][7] = " "
        board[3][8] = " "
        board[3][9] = " "
        board[3][10] = " "
        board[4][6] = " "
        board[4][7] = " "
        board[4][8] = "X"
        board[4][9] = " "
        board[4][10] = " "
        board[5][6] = " "
        board[5][7] = " "
        board[5][8] = " "
        board[5][9] = " "
        board[5][10] = " "
    elif cell == 6:
        board[3][12] = " "
        board[3][13] = " "
        board[3][14] = " "
        board[3][15] = " "
        board[3][16] = " "
        board[4][12] = " "
        board[4][13] = " "
        board[4][14] = "X"
        board[4][15] = " "
        board[4][16] = " "
        board[5][12] = " "
        board[5][13] = " "
        board[5][14] = " "
        board[5][15] = " "
        board[5][16] = " "
    elif cell == 7:
        board[6][0] = " "
        board[6][1] = " "
        board[6][2] = " "
        board[6][3] = " "
        board[6][4] = " "
        board[7][0] = " "
        board[7][1] = " "
        board[7][2] = "X"
        board[7][3] = " "
        board[7][4] = " "
        board[8][0] = " "
        board[8][1] = " "
        board[8][2] = " "
        board[8][3] = " "
        board[8][4] = " "
        #print("### flag ###")
    elif cell == 8:
        board[6][6] = " "
        board[6][7] = " "
        board[6][8] = " "
        board[6][9] = " "
        board[6][10] = " "
        board[7][6] = " "
        board[7][7] = " "
        board[7][8] = "X"
        board[7][9] = " "
        board[7][10] = " "
        board[8][6] = " "
        board[8][7] = " "
        board[8][8] = " "
        board[8][9] = " "
        board[8][10] = " "
    elif cell == 9:
        board[6][12] = " "
        board[6][13] = " "
        board[6][14] = " "
        board[6][15] = " "
        board[6][16] = " "
        board[7][12] = " "
        board[7][13] = " "
        board[7][14] = "X"
        board[7][15] = " "
        board[7][16] = " "
        board[8][12] = " "
        board[8][13] = " "
        board[8][14] = " "
        board[8][15] = " "
        board[8][16] = " "

def scoreO(cell):
    global overallo
    overallo[cell - 1] = "O"
    if cell == 1:
        board[0][0] = " "
        board[0][1] = " "
        board[0][2] = " "
        board[0][3] = " "
        board[0][4] = " "
        board[1][0] = " "
        board[1][1] = " "
        board[1][2] = "O"
        board[1][3] = " "
        board[1][4] = " "
        board[2][0] = " "
        board[2][1] = " "
        board[2][2] = " "
        board[2][3] = " "
        board[2][4] = " "
    elif cell == 2:
        board[0][6] = " "
        board[0][7] = " "
        board[0][8] = " "
        board[0][9] = " "
        board[0][10] = " "
        board[1][6] = " "
        board[1][7] = " "
        board[1][8] = "O"
        board[1][9] = " "
        board[1][10] = " "
        board[2][6] = " "
        board[2][7] = " "
        board[2][8] = " "
        board[2][9] = " "
        board[2][10] = " "
    elif cell == 3:
        board[0][12] = " "
        board[0][13] = " "
        board[0][14] = " "
        board[0][15] = " "
        board[0][16] = " "
        board[1][12] = " "
        board[1][13] = " "
        board[1][14] = "O"
        board[1][15] = " "
        board[1][16] = " "
        board[2][12] = " "
        board[2][13] = " "
        board[2][14] = " "
        board[2][15] = " "
        board[2][16] = " "
    elif cell == 4:
        board[3][0] = " "
        board[3][1] = " "
        board[3][2] = " "
        board[3][3] = " "
        board[3][4] = " "
        board[4][0] = " "
        board[4][1] = " "
        board[4][2] = "O"
        board[4][3] = " "
        board[4][4] = " "
        board[5][0] = " "
        board[5][1] = " "
        board[5][2] = " "
        board[5][3] = " "
        board[5][4] = " "
    elif cell == 5:
        board[3][6] = " "
        board[3][7] = " "
        board[3][8] = " "
        board[3][9] = " "
        board[3][10] = " "
        board[4][6] = " "
        board[4][7] = " "
        board[4][8] = "O"
        board[4][9] = " "
        board[4][10] = " "
        board[5][6] = " "
        board[5][7] = " "
        board[5][8] = " "
        board[5][9] = " "
        board[5][10] = " "
    elif cell == 6:
        board[3][12] = " "
        board[3][13] = " "
        board[3][14] = " "
        board[3][15] = " "
        board[3][16] = " "
        board[4][12] = " "
        board[4][13] = " "
        board[4][14] = "O"
        board[4][15] = " "
        board[4][16] = " "
        board[5][12] = " "
        board[5][13] = " "
        board[5][14] = " "
        board[5][15] = " "
        board[5][16] = " "
    elif cell == 7:
        board[6][12] = " "
        board[6][13] = " "
        board[6][14] = " "
        board[6][15] = " "
        board[6][16] = " "
        board[7][12] = " "
        board[7][13] = " "
        board[7][14] = "O"
        board[7][15] = " "
        board[7][16] = " "
        board[8][12] = " "
        board[8][13] = " "
        board[8][14] = " "
        board[8][15] = " "
        board[8][16] = " "
    elif cell == 8:
        board[6][6] = " "
        board[6][7] = " "
        board[6][8] = " "
        board[6][9] = " "
        board[6][10] = " "
        board[7][6] = " "
        board[7][7] = " "
        board[7][8] = "O"
        board[7][9] = " "
        board[7][10] = " "
        board[8][6] = " "
        board[8][7] = " "
        board[8][8] = " "
        board[8][9] = " "
        board[8][10] = " "
    elif cell == 9:
        board[6][12] = " "
        board[6][13] = " "
        board[6][14] = " "
        board[6][15] = " "
        board[6][16] = " "
        board[7][12] = " "
        board[7][13] = " "
        board[7][14] = "O"
        board[7][15] = " "
        board[7][16] = " "
        board[8][12] = " "
        board[8][13] = " "
        board[8][14] = " "
        board[8][15] = " "
        board[8][16] = " "

def prohibitedRanges(cell):
    global cellDict
    global prohibitedRCs
    for row in range(len(cellDict[cell][0])):
        for col in range(len(cellDict[cell][1])):
            prohibitedRCs.append((cellDict[cell][0][row], cellDict[cell][1][col]))



print('Welcome to ultimate Tic-Tac-Toe!\nCreated by Jackson Ballew')
rules = bool(input("If you would like the rules displayed enter any input. If not, enter no input: "))
if rules == True:
    print("Here are some rules and info on Ultimate tic-tac-toe:")
    print("Ultimate tic-tac-toe (also known as ten-tac-toe, super tic-tac-toe, strategic tic-tac-toe, meta tic-tac-toe, tic-tac-tic-tac-toe-toe, or (tic-tac-toe)²) is a board game composed of nine tic-tac-toe boards arranged in a 3 × 3 grid. Players take turns playing in the smaller tic-tac-toe boards until one of them wins in the larger tic-tac-toe board. Compared to traditional tic-tac-toe, strategy in this game is conceptually more difficult and has proven more challenging for computers.")
    print("Each small 3 × 3 tic-tac-toe board is referred to as a local board, and the larger 3 × 3 board is referred to as the global board. The game starts with X playing wherever they want in any of the 81 empty spots. This move \"sends\" their opponent to its relative location. For example, if X played in the top right square of their local board, then O needs to play next in the local board at the top right of the global board. O can then play in any one of the nine available spots in that local board, each move sending X to a different local board. If a move is played so that it is to win a local board by the rules of normal tic-tac-toe, then the entire local board is marked as a victory for the player in the global board. Once a local board is won by a player or it is filled completely, no more moves may be played in that board. If a player is sent to such a board, then that player may play in any other board. Game play ends when either a player wins the global board or there are no legal moves remaining, in which case the game is a draw.")
    print("DISCLAINER: Unlike in some editions, \"CAT\" games will not be scored for either opponent(future patches may change this). \nFor more info please look at:\nhttps://en.wikipedia.org/wiki/Ultimate_tic-tac-toe\nor\nhttps://ultimate-t3.herokuapp.com/rules")
print('Continueing to the game:')
print("The game board is pictured below:")
while gameActive == True:
    drawBoard()
    oneTurn()
print("The game is over! Thanks for playing!\nCreated by: Jackson Ballew")






