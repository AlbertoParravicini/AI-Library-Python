from TicTacToeState import TicTacToeState
from TicTacToeNode import TicTacToeNode
from TicTacToeProblem import TicTacToeProblem

class TicTacToeGame(object):
    """description of class"""

    def __init__(self):
        self.state = TicTacToeState()
        
        while True:
            print("---------------------------------------------------------------\n")
            print(self.state.board)
            print("\nIt's the turn of ", self.state.curr_player)
            move_valid = False
            while not move_valid:
                try:
                    row = int(input("Tell me a row: "))
                    col = int(input("Tell me a column: "))
                    if {row, col}.issubset(range(0,3)):
                        self.state.make_move(row, col)
                        move_valid = True
                    else:
                        raise ValueError
                except ValueError:
                   print("The move isn't valid!") 

            if not self.state.is_game_over():
                self.state = TicTacToeState(self.state)
            else:
                print("GAME OVER!")
                break
            
        


state = TicTacToeState()
node = TicTacToeNode(state)
#state.make_move(0,0)
#state.make_move(1,1)
#state.make_move(2,2)
#state = TicTacToeState(state)
#state.make_move(2,1)
#state.make_move(1,2)
#print(state.is_game_over())
problem = TicTacToeProblem()
successors = problem.get_successors(node)
for succ in successors:
    print(succ.state.board)
#game = TicTacToeGame()