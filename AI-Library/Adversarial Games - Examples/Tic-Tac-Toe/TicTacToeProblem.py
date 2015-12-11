from AdversarialProblem import AdversarialProblem
from TicTacToeNode import TicTacToeNode, TicTacToeState, Tokens
import numpy as np
import copy as copy

class TicTacToeProblem(AdversarialProblem):
    """description of class"""

    def __init__(self):
        super(AdversarialProblem, self).__init__()
        self.min_value = -10000
        self.max_value = 10000

    def get_successors(self, node):
        successors = []
        for row in range(0,3):
            for col in range(0,3):
                if node.state.board[row][col] == Tokens.empty:
                    curr_succ_state = copy.deepcopy(node.state)
                    curr_succ_state.make_move(row, col)
                    curr_succ_node = TicTacToeNode(TicTacToeState(curr_succ_state), node, "Cell selected: [" + str(row) + ", " + str(col) + "]") 
                    successors.append(curr_succ_node)
        return successors

    def is_end_node(self, node):
        return node.state.is_game_over()

    def value(self, node):
        return self.h1(node)        

    def h1(self, node):
        heuristic_matrix = [[0,  -10, -100, -1000],
                            [10,   0,    0],
                            [100,  0],
                            [1000]] 
        board = node.state.board  
       
        value = 0
        i3 = j3 = i4 = j4 = 0
        for curr_index in range(0,3):
            i1 = j1 = i2 = j2 = 0
         
            i1 = (board[curr_index, :] == Tokens.cross).sum()
            j1 = (board[curr_index, :] == Tokens.circle).sum()
            i2 = (board[:, curr_index] == Tokens.cross).sum()
            j2 = (board[:, curr_index] == Tokens.circle).sum()
            value += heuristic_matrix[i1][j1]
            value += heuristic_matrix[i2][j2]

            if board[curr_index][curr_index] == Tokens.cross:
                i3 += 1
            elif board[curr_index][curr_index] == Tokens.circle:
                j3 += 1 
            if board[2 - curr_index][curr_index] == Tokens.cross:
                i4 += 1
            elif board[2 - curr_index][curr_index] == Tokens.circle:
                j4 += 1 
        value += heuristic_matrix[i3][j3]
        value += heuristic_matrix[i4][j4]    
             
        return value

    def h2(self, node):
        board = node.state.board  
        result = 0
       
        if node.state.has_player_won(Tokens.cross):
            return 1000
        elif node.state.has_player_won(Tokens.circle):
            return -1000

        for curr_index in range(0,3):
            if (board[curr_index, :] == Tokens.cross).sum() >= 1 and (board[curr_index, :] == Tokens.empty).sum() >= 1:
                result += 1
            if (board[curr_index, :] == Tokens.circle).sum() >= 1 and (board[curr_index, :] == Tokens.empty).sum() >= 1:
                result -= 1

            if (board[:, curr_index] == Tokens.cross).sum() >= 1 and (board[:, curr_index] == Tokens.empty).sum() >= 1:
                result += 1
            if (board[:, curr_index] == Tokens.circle).sum() >= 1 and (board[:, curr_index] == Tokens.empty).sum() >= 1:
                result -= 1

        if (np.diag(board) == Tokens.cross).sum() >= 1 and (np.diag(board) == Tokens.empty).sum() >= 1:
             result += 1
        if (np.diag(board) == Tokens.circle).sum() >= 1 and (np.diag(board) == Tokens.empty).sum() >= 1:
            result -= 1 

        if (np.diag(np.fliplr(board)) == Tokens.cross).sum() >= 1 and (np.diag(np.fliplr(board)) == Tokens.empty).sum() >= 1:
            result += 1 
        if (np.diag(np.fliplr(board)) == Tokens.circle).sum() >= 1 and (np.diag(np.fliplr(board)) == Tokens.empty).sum() >= 1:
            result -= 1 
        return result