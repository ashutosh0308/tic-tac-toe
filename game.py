#taking input from user 
def display_board(board):
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('-----------')
    print(board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('-----------')
    print(board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print("\n"*3)
    pass


#Getting input from players
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    pass

#placing the marker on game board
def place_marker(board,marker,position):
    board[position]=marker
    pass

#checking if won
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
    pass


#turn select
import random
def choose_first():
    chance=random.randint(1,2)
    if chance==1:
        return "Player 1 "
    else:
        return "Player 2 "

    pass

#space empty or not
def space_check(board, position):
    if board[position] == '':
        return True
    else:
        return False

    pass

#board full or not
def full_board_check(board):
    count=0
    for item in board:
        if item!='':
            count=count+1

    if count==9:
        return True
    else:
        return False

    pass

#player's move
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        print("\n")

    return position


def replay():
    str=input("Do you want to play again : (Y/N)")
    if str=='Y':
        return True
    else:
        return False

    pass


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [''] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Y or N.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

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


