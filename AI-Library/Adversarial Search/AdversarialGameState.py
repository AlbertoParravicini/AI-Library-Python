from abc import ABCMeta
from abc import abstractmethod

class AdversarialGameState(metaclass=ABCMeta):
    """
    Class used to incapsulate the game state, 
    i.e the current game configuration (e.g. board, scores, players...);
    the game state can be wrapped in an AdversarialGameNode, which also contains
    its parent node and the move that lead to this state. 
    The node can be used in an adversarial search algorithm (e.g. Minimax);
    """
   
    def __init__(self):
        return

