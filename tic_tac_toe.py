# A tic-tac-toe board can be represented as a 3×3 two-dimensional list,
# where zeros mean empty cells, one means X, and two means O. 
# Implement that game using a Python List.

# Welcome players!
print('Welcome to the best game in the world\n\n        TIC_TAC_TOE\n')
# please enter the names
print('Please, enter player names')
player1 = input('player1 :  ')
while True:
    player2 = input('player2 :  ')
    if player2 == player1:
        # names must be different
        print('The names are same, please enter another name')
    else:
        break

# view of the board at the beginning of the game
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# function checks for free cells
def free_cell():
    for i in board:
            if 0 in i:
                return True
    return False            

# This function is called at the very beginning (The call point is at the end of the file)
def play():  
    # until the game has no winner, or until we have a free cell, 
    # the start() function is called for each player in turn
    res = False
    while res == False:
        if res == False and free_cell():
            res = start(1)
        # After each call, we check again for a winner or an empty cell
        if res == False and free_cell():
            res = start(2)
        # if the winner's name is already known, congratulations!
        if res == player1 or res == player2:
            for i in board:
                print(i)
            print('\n       congratulations!!!!!\n')
            print('         The winner is ' + res.upper())
            break
        # if there are no more free cells, the game ends in a draw
        if not free_cell():
            print('the game ended in a tie')
            break
    # offer to play again 
    print('\nwould you like to play again?(y/n)\n')
    while True:
        answer = input()
        if answer.lower() == 'y':
            # if the game is going to start again, we clear the results 
            # of the previous game from the game board
            for i in board:
                for j in range(3):
                    i[j] = 0
            # call the current play() function again
            play()
        elif answer.lower() == 'n':
            # otherwise, say goodbye and exit the game
            print('BYE!!!!!')
            exit()
        else:
            print("your input is not valid, input 'y' or 'n'")

# This function checks the positions, if there is a winning 
# position, returns the name of the winner
def checking(player, board):
    # check the horizontal positions
    for i in board:
        if (i[0] == i[1] and
            i[0] == i[2] and
            i[0] != 0):
            return player
    # check the vertical positions
    for i in range(3):
        if (board[0][i] == board[1][i] and
            board[0][i] == board[2][i] and
            board[0][i] != 0):
            return player
    # check the diagonals
    if (((board[0][0] == board[1][1] and
        board[1][1] == board[2][2]) or
        (board[1][1] == board[0][2] and
        board[1][1] == board[2][0])) and
        board[1][1] != 0):
        return player
    # if no one has won yet, return False
    return False

# this function allows players to select a cell
def choose_cell(player):
    print('\n' + player + ', your turn, please, choose the cell')
    while True:
        try:
            row = int(input('\nrow :     '))
            if not row in (1, 2, 3):
                print("your input for row is not valid, please, input '1', '2' or '3'")
            else:
                break
        except:
            print("your input for row is not valid, please, input '1', '2' or '3'")
    while True:
        try:
            col = int(input('column :  '))
            if int(col) not in (1, 2, 3):
                print("your input for column is not valid, please, input '1', '2' or '3'")
            else:
                break
        except:
            print("your input for row is not valid, please, input '1', '2' or '3'")
    # if the cell is already corrupted, inform
    if board[row - 1][col - 1] != 0:
        print('that cell is already corrupted, please, choose another cell')
        # give the opportunity to choose again
        choose_cell(player)
    else:
        # to display the player's choice on the board
        if player == player1:   
            board[row - 1][col - 1] = 1
        elif player == player2:
            board[row - 1][col - 1] = 2
    # check the positions, if there is a win, return the name of the winner
    winner = checking(player, board)
    return winner
    

# This function displays the game board and adjusts the turns
def start(turn): 
    print('\n')  
    for i in board:
        print(i)
    if turn == 1:
        res = choose_cell(player1)
    else:
        res = choose_cell(player2)
    return res

# let's start the game
play()