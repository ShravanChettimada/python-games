def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def is_valid_move(move):
    return move.isdigit() and 1 <= int(move) <= 9

def convert_move(move):
    moves_mapping = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }
    return moves_mapping[move]

def play_tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X  |  Player 2: O")
    print_board([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

    current_player = 'X'
    board = [[' ']*3 for _ in range(3)]
    winner = None

    while not winner and not is_board_full(board):
        print(f"Player {current_player}'s turn.")
        move = input("Enter your move (1-9): ")

        if not is_valid_move(move):
            print("Invalid move! Please enter a number between 1 and 9.")
            continue

        row, col = convert_move(move)

        if board[row][col] != ' ':
            print("That position is already taken. Choose another.")
            continue

        board[row][col] = current_player
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Congratulations! Player {winner} wins!")
        elif is_board_full(board):
            print("It's a draw!")

        current_player = 'O' if current_player == 'X' else 'X'

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_tic_tac_toe()
    else:
        print("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()
