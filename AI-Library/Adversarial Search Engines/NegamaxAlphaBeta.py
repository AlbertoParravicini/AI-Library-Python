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

    Parameters:
    -------------
    search_depth: the new maximum depth of the search tree;
                  by default it is equal to 1;
    order_moves: boolean flag which tells if the successors should be ordered
                 based on their immediate value; ordering them takes time but 
                 can reduce the number of visited states, and improve the performances
                 of the search; by default it is set ot False;
    """
    
    def __init__(self, problem, **kwargs):
        super().__init__(problem, **kwargs)
        self.order_moves = kwargs.get("order_moves", False)
    
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
        
        
        self.obtained_value = self.__negamax_ab(initial_node, 0, alpha, beta) if initial_node.is_max() else -self.__negamax_ab(initial_node, 0, alpha, beta)  

        self.search_performed = True


    def __negamax_ab(self, node, depth, alpha, beta):
        if depth >= self.search_depth or self.problem.is_end_node(node):
            # Checking the parent instead of the current node allows to have a non-strict Min-Max alternation.
            # The value is not evaluated globally, but from the point of view of the current player;
            return self.problem.value(node) if node.parent_node.is_min() else -self.problem.value(node)
        
        best_value = self.problem.min_value
        # Generates the immediate successors of the node.
        # The moves are ordered based on their immediate value,
        # which reduces the number of visited states;
        successors = self.problem.get_successors(node)
        if self.order_moves:
            sorted(successors, key = lambda n: self.problem.value(n))
        for curr_succ in successors:
            self.num_of_visited_states += 1
            value = -self.__negamax_ab(curr_succ, depth + 1, -beta, -alpha)
            if best_value < value:
                best_value = value   
                # If a new best move was found, save it;             
                if depth == 0:
                    self.obtained_successor = curr_succ
            
            # The window is restricted from left to right,
            # by increasing the value of alpha, the higher lowest bound.
            alpha = max(value, alpha)
            # If the window has negative width, the branch is cut,
            # and the value of the node returned to its parent;
            if alpha >= beta:
                break
        return best_value


   