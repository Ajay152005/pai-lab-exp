import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    #check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3) or all(board[i][2-i] == player for i in range(3))):
        return True
    return False

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j]== " "]

def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return -10 + depth, None
    elif check_winner(board, "O"):
        return 10 -depth, None
    elif len(available_moves(board)) == 0:
        return 0, None

    if maximizing_player:
        max_eval = float("-inf")
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = "O"
            eval, _ = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            eval, _ = minimax(board, depth+1, True)
            board[move[0]][move[1]] = " "
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

def ai_move(board):
    _, move = minimax(board, 0, True)
    return move

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <=2 and board[row][col] == " ":
                return row, col
            else:
                print('Invalid move, Try again.')
        except ValueError:
            print("Invalid input. Please enter integers.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        print("Your turn: ")
        row, col = player_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        # AI's move
        print("AI's turn: ")
        row, col = ai_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins!")
            break
        if len(available_moves(board)) == 0:
            print("It's a draw!")
            break
play_game()
        