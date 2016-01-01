from AdversarialSearchEngine import AdversarialSearchEngine
import random as random

class MinimaxAlphaBeta(AdversarialSearchEngine):
    """
    Implementation of the Minimax algorithm with alpha-beta pruning.
    The algorithm works for zero-sum, two-players, turn-based games, with perfect knowledge and deterministic moves.
    Given an initial node, it will look for the best move that the current player can perform,
    under the assumption that both players will play rationally (i.e optimally).
    Alpha-beta pruning optimizes the search by discarding branches which are guaranteed to return 
    values worse than the current result.
    Minimax with alpha-beta pruning should be preferred over the standard minimax 
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
        
        self.obtained_successor = None
        self.obtained_value = alpha if initial_node.is_max() else beta

        # If the maximum depth is set to 0, return a random successor node;
        if self.search_depth == 0:
            self.obtained_successor = random.choice(self.problem.get_successors(initial_node))
            self.obtained_value = self.problem.value(self.obtained_successor)
            return
        
        # Generates the immediate successors of the initial node,
        # then apply a minimax search to each of them:
        # their values, along with alpha and beta, are passed up to the highest level;
        # The moves are ordered based on their immediate value,
        # which reduces the number of visited states;
        successors = self.problem.get_successors(initial_node)
        if self.order_moves:
            successors.sort(key=lambda n: self.problem.value(n), reverse = initial_node.is_max())

        for curr_succ in successors:
            
            self.num_of_visited_states += 1
            # A certain player might play more than one turn in a row, 
            # so no assumptions are made with respect to the turn alternation;
            if curr_succ.is_max():
                result = self.__minimax_ab(curr_succ, 1, self.problem.min_value, self.obtained_value)
            else:
                result = self.__minimax_ab(curr_succ, 1, self.obtained_value, self.problem.max_value)

            # If a new best move was found, save it along with the value provided by the search;
            if (initial_node.is_max() and result > self.obtained_value) or (initial_node.is_min() and result < self.obtained_value):
                self.obtained_value = result
                self.obtained_successor = curr_succ
        self.search_performed = True


    def __minimax_ab(self, node, depth, alpha, beta):
        if depth >= self.search_depth or self.problem.is_end_node(node):
            return self.problem.value(node)
        
        
        if node.is_max():
            value = alpha
            for curr_succ in self.problem.get_successors(node):
                self.num_of_visited_states += 1
                # Update the current value of the node; Max will always take the node with highest value;
                # beta remains fixed, as it won't be allowed to get a value higher than it;                
                value = max(value, self.__minimax_ab(curr_succ, depth + 1, alpha, beta))
            
                # If the value found is outside the window, the branch is cut,
                # and the value of the node returned to its parent;
                if value >= beta:
                    return value
            
                # The window is restricted by Max from left to right,
                # by increasing the value of alpha, the higher lowest bound.
                # It means that max will always be able to perform a move 
                # whose value is equal to alpha;
                alpha = max(alpha, value)
            # If all the successors have been visited, return the value of the node,    
            # which is guaranteed to be between alpha and beta;      
            return value

        else:      
            value = beta
            for curr_succ in self.problem.get_successors(node):
                self.num_of_visited_states += 1
                # Update the current value of the node; Min will always take the node with lowest value;
                # alpha remains fixed, as it won't be allowed to get a value lower than it; 
                if curr_succ.is_max():
                    value = min(value, self.__minimax_ab(curr_succ, depth + 1, alpha, beta))
            
                # If the value found is outside the window, the branch is cut,
                # and the value of the node returned to its parent;
                if value <= alpha:
                    return value
                
                # The window is restricted by Min from right to left,
                # by increasing the value of beta, the lower highest bound.
                # It means that min will always be able to perform a move 
                # whose value is equal to beta;
                beta = min(beta, value)
            # If all the successors have been visited, return the value of the node,    
            # which is guaranteed to be between alpha and beta;   
            return value

    def set_order_moves(self, choice):
        """
        Set if the successors of a node should be ordered based on their immediate value;
    
        Parameters:
        -------------
        choice: boolean variable, it tells if the moves should be ordered or not;
        """
        try:
            if not isinstance(choice, bool):
                raise TypeError
            assert not self.search_performed
            self.order_moves = choice
        except TypeError:
                print("ERROR: ", choice, " isn't a boolean variable!")
        except AssertionError:
                print("ERROR: serach already performed!")
            



