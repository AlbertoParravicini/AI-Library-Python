from AdversarialGameState  import AdversarialGameState
from enum import Enum
import numpy as np
import random as random
import copy as copy

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
            self.board = copy.copy(parent.board)
            self.curr_player = Tokens.cross if parent.curr_player == Tokens.circle else Tokens.circle

    def make_move(self, row, col):          
        if row not in range(0,3) or col not in range(0,3) or self.board[row, col] != Tokens.empty:
            raise ValueError
        else:
            self.board[row, col] = self.curr_player
       

    def is_game_over(self):          
        return self.has_player_won(Tokens.cross) or self.has_player_won(Tokens.circle) or (Tokens.empty not in self.board.reshape(-1))

    def has_player_won(self, player_token):
        # A fast but not particularly pretty approach:
        sum_diag_1 = 0
        sum_diag_2 = 0
        for curr_index in range(0,3):
            sum_row = 0
            sum_col = 0
            for sec_index in range(0,3):
                if self.board[curr_index, sec_index] == player_token:
                    sum_row += 1
                if self.board[sec_index, curr_index] == player_token:
                    sum_col += 1
            if sum_row == 3 or sum_col == 3:
                return True
            if self.board[curr_index, curr_index] == player_token:
                sum_diag_1 += 1
            if self.board[2 -curr_index, curr_index] == player_token:
                sum_diag_2 += 1
        if sum_diag_1 == 3 or sum_diag_2 == 3:
            return True   
        return False
           
    def set_curr_player(self, new_player):
        try:
            if new_player not in {Tokens.cross, Tokens.circle}:
                raise ValueError
            self.curr_player = new_player
        except ValueError:
            print("The player isn't valid!")

    def __str__(self):
        string = ""
        string += " -------------\n" 
        for row in range(0,3):
            string += " |"
            for col in range(0,3):              
                if self.board[row][col] == Tokens.circle:
                    string += " O "
                elif self.board[row][col] == Tokens.cross:
                    string += " X "
                else:
                    string += "   "
                string += "|"
            string += "\n -------------\n" 
        return string

    def __eq__(self, another_state):
        return np.array_equal(self.board, another_state.board)
