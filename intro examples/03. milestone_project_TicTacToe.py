import random

## print out a board.
def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("- - - - -")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("- - - - -")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# test 
# board = ['#','1','2','3','4','5','6','7','8','9']  
# display_board(board)

## take in a player input and assign their marker as 'X' or 'O'. 
def player_input():
# Returns a touple (Player 1 marker, Player 2 marker)
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose your marker (X or O): ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#player_input()  

# Unpack the touple returned from player_input(), whilst running the above function
p1_marker, p2_marker = player_input()

## takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board,marker,position):
    board[position]=marker

# test
# place_marker(board,'X',1)  
# display_board(board)     

## checks to see if that mark has won.
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

## randomly decide which player goes first. 
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    
## returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    
    return board[position] == ' '
    
# choose_first() # test 

## checks if the board is full and returns a boolean value.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True  # Board is FULL if we return True

## asks for a player's next position (as a number 1-9) and then uses space_check() to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

## asks the player if they want to play again
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


## GAME SEQUENCE

print('Welcome to Tic Tac Toe!')

while True:

    # SET UP
    theBoard = [' '] * 10                                   # Reset the board as a series of empty strings
    player1_marker, player2_marker = player_input()         # Define which marker belongs to which player
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Y or N.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    # Gameplay
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
