from AdversarialSearchEngine import AdversarialSearchEngine
import random as random
import numpy

class MinimaxAlphaBeta(AdversarialSearchEngine):
    """
    Implementation of the Minimax algorithm with alpha-beta pruning.
    The algorithm works for zero-sum, two-players, turn-based games, with perfect knowledge and deterministic moves.
    Given an initial node, it will look for the best move that the current player can perform,
    under the assumption that both players will play rationally (i.e optimally).
    Alpha-beta pruning optimizes the search by discarding branches which are guaranteed to return 
    values worse than the current result.
    On average, the performance gain over the standard minimax is about 50%;
    Minimax with alpha-beta pruning should be preferred over the standard minimax 
    in every case but the simplest problems, 
    as it doesn't pose any practical disadvantage over the standard Minimax;
    """
    
    def __init__(self, problem, search_depth = 1):
        super().__init__(problem, search_depth)
    
    def perform_search(self, initial_node):  
        """
        Perform a search from the provided initial_node, by using the rules
        expressed in the associated problem.
        The result of the search will be stored in obtained_result and obtained_successor.
        If the initial_node has no successors, the obtained_successor will be None,
        and obtained_result will be calculated on the initial_node;

        Parameters:
        -------------
        initial_node: the node from which the search starts;
        """
        
        self.obtained_successor = None
        self.obtained_value = self.problem.min_value if initial_node.is_max() else self.problem.max_value
        alpha = self.problem.min_value
        beta = self.problem.max_value

        # If the maximum depth is set to 0, return a random successor node;
        if self.search_depth == 0:
            self.obtained_successor = random.choice(self.problem.get_successors(initial_node))
            self.obtained_value = self.problem.value(self.obtained_successor)
        else:
            self.initial_node = initial_node
            self.obtained_value = self.minimax_ab(initial_node, alpha, beta, 0)
            while (self.obtained_successor.parent_node != initial_node):
                self.obtained_successor = self.obtained_successor.parent_node
        self.search_performed = True


    def minimax_ab(self, node, alpha, beta, depth):
        if depth >= self.search_depth or self.problem.is_end_node(node):
            #print("VALUE: ", self.problem.value(node), "depth: ", depth)
            return self.problem.value(node)


        if node.is_max():
            for curr_succ in self.problem.get_successors(node):  
                #self.log(curr_succ, alpha, beta, depth)         
                value = self.minimax_ab(curr_succ, alpha, beta, depth + 1)
                
                if value > alpha:
                    if self.initial_node.is_max() and value <= beta:
                        self.obtained_successor = curr_succ
                    alpha = value

                if beta <= alpha:
                    return alpha
            return value


        else:
            for curr_succ in self.problem.get_successors(node):
                #self.log(curr_succ, alpha, beta, depth)
                value = self.minimax_ab(curr_succ, alpha, beta, depth + 1)
                if value < beta:
                    if self.initial_node.is_min() and alpha <= value:
                        self.obtained_successor = curr_succ
                    beta = value

                if beta <= alpha:
                    return beta
            return value

    def log(self, node, alpha, beta, depth):
        print(node.rule_applied, node.state, "alpha: ", alpha, ", beta: ", beta, " depth: ", depth, "\n-----------------\n")
       