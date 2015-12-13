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
        curr_depth = 0
        alpha = self.problem.min_value
        beta = self.problem.max_value

        for curr_succ in self.problem.get_successors(initial_node):
            # If the maximum depth is set to 0, return a random successor node;
            if self.search_depth == 0:
                self.obtained_successor = random.choice(self.problem.get_successors(initial_node))
                self.obtained_value = self.problem.value(self.obtained_successor)
                break
            
            # A certain player might play more than one turn in a row, 
            # so no assumptions are made with respect to the turn alternation;
            if curr_succ.is_max():
                result = self.__max(curr_succ, curr_depth + 1, alpha, self.obtained_value)
            else:
                result = self.__min(curr_succ, curr_depth + 1, self.obtained_value, beta)

            # If a new best move was found, save it along with the value provided by the search;
            if (initial_node.is_max() and result > self.obtained_value) or (initial_node.is_min() and result < self.obtained_value):
                self.obtained_value = result
                self.obtained_successor = curr_succ
        self.search_performed = True

    def __max(self, node, depth, alpha, beta):
        """
        Max will examine the successors of the current node and keep the one with highest value;
        """
        if self.problem.is_end_node(node) or depth == self.search_depth:
            return self.problem.value(node)
        
        value = alpha
        for curr_succ in self.problem.get_successors(node):
            if curr_succ.is_max():
                result = self.__max(curr_succ, depth + 1, value, beta)
            else:
                result = self.__min(curr_succ, depth + 1, value, beta)
            # If the result is out of bounds, the branch is abandoned; the value of the node is returned anyway;
            if result >= beta:
                return result
            # Update the current value of the node; Max will always take the node with highest value;
            value = max(result, value) 
        return value


    def __min(self, node, depth, alpha, beta):
        """
        Min will examine the successors of the current node and keep the one with lowest value;
        """
        if self.problem.is_end_node(node) or depth == self.search_depth:
            return self.problem.value(node)
        
        value = beta
        for curr_succ in self.problem.get_successors(node):
            if curr_succ.is_max():
                result = self.__max(curr_succ, depth + 1, alpha, value)
            else:
                result = self.__min(curr_succ, depth + 1, alpha, value)
            # If the result is out of bounds, the branch is abandoned; the value of the node is returned anyway;
            if result <= alpha:
                return result   
            # Update the current value of the node; Min will always take the node with lowest value;
            value = min(result, value)     
        return value

    





