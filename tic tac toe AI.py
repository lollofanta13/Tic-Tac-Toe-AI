# Import the necessary libraries
import random

# Define the Tic Tac Toe board and player symbols
board = [' '] * 9
player_symbol = 'X'
computer_symbol = 'O'

# Define the function to display the Tic Tac Toe board
def display_board():
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

# Define the function to check if the game is over
def game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    # Check if board is full
    if ' ' not in board:
        return True
    return False

# Define the function to get the player's move
def get_player_move():
    while True:
        move = input('Enter your move (1-9): ')
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == ' ':
            return int(move) - 1
        print('Invalid move. Please try again.')

# Define the function to get the computer's move
def get_computer_move():
    # Random move
    move = random.randint(0, 8)
    if board[move] == ' ':
        return move
    # Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer_symbol
            if game_over():
                board[i] = ' '
                return i
            board[i] = ' '
    # Try to block
    for i in range(9):
        if board[i] == ' ':
            board[i] = player_symbol
            if game_over():
                board[i] = ' '
                return i
            board[i] = ' '
    # Random move
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            return move

# Define the function to play the game
def play_game():
    global board
    board = [' '] * 9
    while not game_over():
        display_board()
        player_move = get_player_move()
        board[player_move] = player_symbol
        if game_over():
            break
        computer_move = get_computer_move()
        board[computer_move] = computer_symbol
    display_board()
    if ' ' not in board:
        print('Tie game!')
    elif board.count(player_symbol) > board.count(computer_symbol):
        print('You win!')
    else:
        print('Computer wins!')

# Play the game
play_game()
