"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x +=1
            elif cell == O:
                count_o +=1
    if count_x > count_o:
        return O
    return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    answer = []
    
    for i in range(0,3) :
        for j in range(0,3):
            if board[i][j] == None:
                answer.append((i,j))
    return answer
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    new_board = [row[:] for row in board]  # Deep copy of board
    new_board[i][j] = player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][2] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[2][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    have to check if there is a winner or if it is full
    """
    if winner(board) is not None:
        return True
    
    return all(cell is not None for row in board for cell in row)
            
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    1. get every action 
    2. minimax that action 
    3. choose the max possible action 
    """
    # if terminal(board):  
    if terminal(board):
        return None
    toPlay = player(board)
    actiones = actions(board)
    best_action = None

    if toPlay == X:
        # we want to maximize
        best_value = -math.inf
        for action in actiones:
            value = minimize(result(board, action ))
            if best_value < value :
                best_value = value
                best_action = action 
    else:
        best_value = math.inf
        for action in actiones:
            value = maximize(result(board, action ))
            if best_value > value :
                best_value = value
                best_action = action 
    
    return best_action

    raise NotImplementedError



def maximize(board):
    if terminal(board):
        return utility(board)
    best_value = -math.inf
    for action in actions(board):
        best_value = max(best_value,minimize(result(board, action)))
    return best_value 


def minimize(board):
    if terminal(board):
        return utility(board)
    best_value = math.inf
    for action in actions(board):
        best_value = min(best_value,maximize(result(board, action)))
    return best_value 
            
 