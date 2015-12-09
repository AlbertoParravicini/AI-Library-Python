from AdversarialProblem import AdversarialProblem
from TicTacToeNode import TicTacToeNode, TicTacToeState, Tokens

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
                    curr_succ_state = TicTacToeState(node.state)
                    curr_succ_state.make_move(row, col)
                    curr_succ_node = TicTacToeNode(curr_succ_state, node, "Cell selected: [" + str(row) + ", " + str(col) + "]") 
                    successors.append(curr_succ_node)
        return successors

    def is_end_node(self, node):
        return node.state.is_game_over()

    def value(self, node):
        heuristic_matrix = [[0,  -10, -100, -1000],
                            [10,   0,    0,     0],
                            [100,  0,    0,     0],
                            [1000, 0,    0,     0]]  
        board = node.state.board  
       
        value = 0
        for curr_row in range(0,3):
            i = 0
            j = 0
            for curr_col in range(0,3):
                if board[curr_row][curr_col] == Tokens.cross:
                    i += 1
                elif board[curr_row][curr_col] == Tokens.circle:
                    j += 1
            value += heuristic_matrix[i][j]
        
       
        for curr_col in range(0,3):
            i = 0
            j = 0
            for curr_row in range(0,3):
                if board[curr_row][curr_col] == Tokens.cross:
                    i += 1
                elif board[curr_row][curr_col] == Tokens.circle:
                    j += 1
            value += heuristic_matrix[i][j]
        
        i = 0
        j = 0
        for curr_ind in range(0,3):    
            if board[curr_ind][curr_ind] == Tokens.cross:
                i += 1
            elif board[curr_ind][curr_ind] == Tokens.circle:
                j += 1
        value += heuristic_matrix[i][j]
        i = 0
        j = 0
        for curr_ind in range(0,3):    
            if board[2 - curr_ind][curr_ind] == Tokens.cross:
                i += 1
            elif board[2 - curr_ind][curr_ind] == Tokens.circle:
                j += 1
        value += heuristic_matrix[i][j]
             
        return value
