from AdversarialSearchEngine import AdversarialSearchEngine
import random as random

class NegamaxAlphaBeta(AdversarialSearchEngine):
    """
    Implementation of the Negamax algorithm with alpha-beta pruning.
    The Negamax works exactly like the standard minimax, it only has fewer lines of code.
     The algorithm works for zero-sum, two-players, turn-based games, with perfect knowledge and deterministic moves.
    Given an initial node, it will look for the best move that the current player can perform,
    under the assumption that both players will play rationally (i.e optimally).
    Alpha-beta pruning optimizes the search by discarding branches which are guaranteed to return 
    values worse than the current result.
    Negamax with alpha-beta pruning should be preferred over the standard minimax 
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
        
        alpha = self.problem.min_value
        beta = self.problem.max_value
        self.obtained_successor = None
        self.obtained_value = alpha if initial_node.is_max() else beta

        # If the maximum depth is set to 0, return a random successor node;
        if self.search_depth == 0:
            self.obtained_successor = random.choice(self.problem.get_successors(initial_node))
            self.obtained_value = self.problem.value(self.obtained_successor)
            return
        
        self.obtained_value = self.__negamax_ab(initial_node, 0) if initial_node.is_max() else -self.__negamax_ab(initial_node, 0)  

        self.search_performed = True


    def __negamax_ab(self, node, depth):
        if depth >= self.search_depth or self.problem.is_end_node(node):
            # Checking the parent instead of the current node allows to have a non-strict Min-Max alternation.
            # The value is not evaluated globally, but from the point of view of the current player;
            return self.problem.value(node) if node.parent_node.is_min() else -self.problem.value(node)
        
        best_value = self.problem.min_value
        for curr_succ in self.problem.get_successors(node):
            self.num_of_visited_states += 1
            value = -self.__negamax_ab(curr_succ, depth + 1)
            if value > best_value:
                best_value = value
                
                if depth == 0:
                    self.obtained_successor = curr_succ
       
        return best_value


        ## Generates the immediate successors of the initial node,
        ## then apply a minimax search to each of them:
        ## their values, along with alpha and beta, are passed up to the highest level;
        ## The moves are ordered based on their immediate value,
        ## which reduces the number of visited states;
        #successors = self.problem.get_successors(initial_node)
        #sorted(successors, key = lambda n: self.problem.value(n))
       
        #for curr_succ in successors:
            
        #    self.num_of_visited_states += 1
        #    if curr_succ.is_max():
        #        result = self.__minimax_ab(curr_succ, 1, alpha, self.obtained_value)
        #    else:
        #        result = self.__minimax_ab(curr_succ, 1, self.obtained_value, beta)

        #    # If a new best move was found, save it along with the value provided by the search;
        #    if (initial_node.is_max() and result > self.obtained_value) or (initial_node.is_min() and result < self.obtained_value):
        #        self.obtained_value = result
        #        self.obtained_successor = curr_succ