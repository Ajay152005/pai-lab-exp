#minimax algorithm for tic-tac-toe

import math

MAX_PLAYER = 'X'
MIN_PLAYER = 'O'
EMPTY = ' '

def evaluate(state):
    if is_winner(state, MAX_PLAYER):
        return 10
    elif is_winner(state, MIN_PLAYER):
        return -10
    elif is_board_full(state):
        return 0
    else:
        return None

def minimax(state, player, max_depth):
    if max_depth == 0 or evaluate(state) is not None:
        return evaluate(state), None
    if player == MAX_PLAYER:
        best_value = float('-inf')
        best_move = None
        for move in legal_moves(state):
            new_state = apply_move(state, move, player)
            value, _ = minimax(new_state, MIN_PLAYER, max_depth - 1)
            if value > best_value:
                best_value = value
                best_move = move
        return best_value, best_move
    else:
        best_value = float('inf')
        best_move = None
        for move in legal_moves(state):
            new_state = apply_move(state, move, player)
            value, _ = minimax(new_state, MAX_PLAYER, max_depth -1)
            if value < best_value:
                best_value = value
                best_move = move
        return best_value, best_move
    
def opponent(player):
    return MIN_PLAYER if player == MAX_PLAYER else MAX_PLAYER

def terminal_state(state):
    return evaluate(state) is not None

def legal_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                moves.append((i, j))
    return moves

def apply_move(state, move, player):
    new_state = [row[:] for row in state]
    i, j = move

    new_state[i][j] = player
    return new_state

def is_winner(state, player):
    lines = (
        #Rows
        state[0], state[1], state[2],

        #columns

        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],

        #diagonals 
        [state[0][0], state[1][1], state[2][2]],
        [state[0][2], state[1][1], state[2][0]]
    )

    return [player, player, player] in lines

def is_board_full(state):
    for row in state:
        if EMPTY in row:
            return False
    return True

if __name__ == "__main__":
    game_state = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY,EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    max_depth = 9

    best_value, best_move = minimax(game_state, MAX_PLAYER, max_depth)
    print("Best value: ", best_value)
    print('Best move: ', best_move)