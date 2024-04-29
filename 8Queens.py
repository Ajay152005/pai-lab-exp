import random

def is_safe(board, row, column):
    for i in range(row):
        if board[i] == column or abs(i - row) == abs(board[i] - column):
            return False
    return True

def attacking_queens(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                attacks += 1
    return attacks

def hill_climbing(n):
    board = [random.randint(0, n-1) for _ in range(n)]
    attacks = attacking_queens(board)
    while True:
        min_attacks = attacks
        next_board = list(board)
        for row in range(n):
            for col in range(n):
                if board[row] != col:
                    next_board[row] = col
                    new_attacks = attacking_queens(next_board)
                    if new_attacks < min_attacks:
                        min_attacks = new_attacks
                        board = list(next_board)
                    if min_attacks == attacks:
                        break
            if min_attacks == attacks:
                break
        if min_attacks == attacks:
            break
        attacks = min_attacks
    return board

def solve_n_queens(num_queens):
    board = [-1] * 8  # Fixed size of 8x8 chessboard
    def backtrack(row):
        nonlocal board
        if row == num_queens:
            return True
        for col in range(8):
            if is_safe(board, row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False
    if backtrack(0):
        return board
    else:
        return None

def print_board(board):
    if board is None:
        print('Solution does not exist')
    else:
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row] == col:
                    print('Q', end='')
                else:
                    print("-", end="")
            print()

def main():
    num_queens = int(input("Enter the number of queens: "))
    if num_queens <= 8:
        solution = solve_n_queens(num_queens)
        print('Solution: ')
        print_board(solution)
    else:
        print("Number of queens should be less than or equal to 8.")

if __name__ == "__main__":
    main()
