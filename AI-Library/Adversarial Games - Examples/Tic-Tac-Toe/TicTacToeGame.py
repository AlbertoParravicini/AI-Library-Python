from TicTacToeState import TicTacToeState, Tokens
from TicTacToeNode import TicTacToeNode
from TicTacToeProblem import TicTacToeProblem
from Minimax import Minimax
from MinimaxAlphaBeta import MinimaxAlphaBeta
import os
import time



class TicTacToeGame(object):
    """description of class"""

    def __init__(self):
        return
            
        
    def human_vs_human(self):
        self.state = TicTacToeState()
        
        while True:
            print("---------------------------------------------------------------\n")
            print(self.state)
            print("It's the turn of ", self.state.curr_player)
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
        engine = MinimaxAlphaBeta(problem, 4)
        
        current_node = initial_node
 
        while not problem.is_end_node(current_node):
            engine.reset_engine()
            print("\n---------------------------------------------------------------")
            print("\nIt's the turn of ", current_node.state.curr_player, "\n")
            print(current_node.state)
                               
            engine.perform_search(current_node)           
            current_node = engine.obtained_successor
            print("Obtained value: ", engine.obtained_value)
            print("Visited states; ", engine.num_of_visited_states, "\n")
            time.sleep(0)
            clear = lambda: os.system('cls')
            #clear()
 
            

        print("\n------------------------------------------------------------")
        print("------------------------ GAME OVER! ------------------------")
        print("------------------------------------------------------------\n")
        print(current_node.state)
        print("Obtained value: ", engine.obtained_value, "\n")
            
        
            

#state = TicTacToeState()
#node = TicTacToeNode(state, None, None)
#problem = TicTacToeProblem()
#state.set_curr_player(Tokens.cross)
#state.make_move(0,0)
#state.make_move(1,1)
#state.set_curr_player(Tokens.circle)
#state.make_move(0,1)
#state.make_move(2,1)

#engine = Minimax(problem, 1)
#engine.perform_search(node)
#succ_list = problem.get_successors(node)
#succ_list = problem.get_successors(succ_list[0])
#succ_list = problem.get_successors(succ_list[0])
#succ_list = problem.get_successors(succ_list[0])

#print(engine.obtained_successor.state)
#print(engine.obtained_value)

#for succ in succ_list:
#   print(succ.state, "Value: ", problem.value(succ))

game = TicTacToeGame()
game.ai_vs_ai()


