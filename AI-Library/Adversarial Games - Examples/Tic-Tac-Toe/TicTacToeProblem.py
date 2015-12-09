from AdversarialProblem import AdversarialProblem
from TicTacToeNode import TicTacToeNode, TicTacToeState, Tokens

class TicTacToeProblem(AdversarialProblem):
    """description of class"""

    def __init__(self):
        super(AdversarialProblem, self).__init__()
        self.min_value = -1000
        self.max_value = 1000

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
        return super().value(node)
