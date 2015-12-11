from AdversarialNode import AdversarialNode
from TicTacToeState import TicTacToeState, Tokens

class TicTacToeNode(AdversarialNode):
    """description of class"""

    def __init__(self, state = None, parent_node = None, rule_applied = None):
        return super().__init__(state, parent_node, rule_applied)    

    def is_max(self):
        return self.state.curr_player == Tokens.cross

    def is_min(self):
        return not self.is_max()