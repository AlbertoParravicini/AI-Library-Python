from AdversarialGameState  import AdversarialGameState
from enum import Enum
import numpy as np
import random as random

class Tokens(Enum):
    circle = 0
    cross = 1
    empty = -1

class TicTacToeState(AdversarialGameState):
    """description of class"""
    
    def __init__(self, parent = None):
        if parent is None:
            self.board = np.full((3,3), Tokens.empty, dtype=Tokens)
            self.curr_player = random.choice([Tokens.cross, Tokens.circle])
        else:
            self.board = parent.board
            self.curr_player = Tokens.cross if parent.curr_player == Tokens.circle else Tokens.circle

    def make_move(self, row, col):   
        try:    
            if row not in range(0,3) or col not in range(0,3) or self.board[row, col] != Tokens.empty:
                raise ValueError
            else:
                self.board[row, col] = self.curr_player
        except ValueError:
            print("The cell isn't valid!")

    def is_game_over(self):          
        return self.has_player_won(Tokens.cross) or self.has_player_won(Tokens.circle) or (Tokens.empty not in self.board.reshape(-1))

    def has_player_won(self, player_token):
        for curr_index in range(0,3):
            if (self.board[curr_index, :] == player_token).sum() == 3 or (self.board[:, curr_index] == player_token).sum() == 3:
                return True
        if (np.diag(self.board) == player_token).sum() == 3 or (np.diag(np.fliplr(self.board)) == player_token).sum() == 3:
            return True  
        return False
           
    def set_curr_player(self, new_player):
        try:
            if new_player not in {Tokens.cross, Tokens.circle}:
                raise ValueError
            self.curr_player = new_player
        except ValueError:
            print("The player isn't valid!")
