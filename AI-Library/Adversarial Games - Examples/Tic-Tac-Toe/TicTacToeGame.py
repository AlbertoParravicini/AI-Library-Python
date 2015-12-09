from TicTacToeState import TicTacToeState
from TicTacToeNode import TicTacToeNode
from TicTacToeProblem import TicTacToeProblem
from Minimax import Minimax

class TicTacToeGame(object):
    """description of class"""

    def __init__(self):
        return
            
        
    def human_vs_human(self):
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
        
    def ai_vs_ai(self):
        initial_state = TicTacToeState()
        initial_node = TicTacToeNode(initial_state)
        problem = TicTacToeProblem()
        engine = Minimax(problem, 6)
        
        current_node = initial_node
 
        while not problem.is_end_node(current_node):
            print("---------------------------------------------------------------")
            print("\nIt's the turn of ", current_node.state.curr_player, "\n")
            print(current_node.state)
                               
            engine.perform_search(current_node)           
            current_node = engine.obtained_successor
            print("Obtained value: ", engine.obtained_value, "\n")

        print("------------------------ GAME OVER! ------------------------")
        print(current_node.state)
        print("Obtained value: ", engine.obtained_value, "\n")
            
        
            




game = TicTacToeGame()
game.ai_vs_ai()