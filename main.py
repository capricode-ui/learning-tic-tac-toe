# Reuse the board and functions from previous milestones
board = [' ' for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def player_move(player_symbol):
    while True:
        try:
            move = int(input(f"Enter your move (1-9) for '{player_symbol}': ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Choose a number from 1 to 9.")
            elif board[move] != ' ':
                print("That spot is already taken. Choose another.")
            else:
                board[move] = player_symbol
                break
        except ValueError:
            print("Please enter a valid number.")

def check_win(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

def play_game():
    #sample comment
    current_player = 'X'
    for turn in range(9):
        display_board()
        player_move(current_player)
        if check_win(current_player):
            display_board()
            print(f"Player '{current_player}' wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'
    display_board()

# Start the game
play_game()
#this is a sample comment just for checking