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
    toPlay = player(board)
    board[i][j] = toPlay
    return board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]  :
        return board[1][1]
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    have to check if there is a winner or if it is full
    """
    for i in range(0,3):
        #if there is a winner return true in terminal
        if (board[i][0] == board[i][1] == board[i][2] is not None )or (board[0][i] == board[1][i] == board[2][i] is not None):
            return True
    if board[0][0] == board[1][1] == board[2][2] is not None or board[0][2] == board[1][1] == board[2][0] is not None :
        return True
    else:
        #if there is no empty cell return true in terminal state
        for list in board:
            if None in list:
                return False
        return True
            
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner == winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError

