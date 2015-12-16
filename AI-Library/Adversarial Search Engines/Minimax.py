from AdversarialSearchEngine import AdversarialSearchEngine
import random as random

class Minimax(AdversarialSearchEngine):
    """
    Implementation of the standard Minimax algorithm.
    The algorithm works for zero-sum, two-players, turn-based games, with perfect knowledge and deterministic moves.
    Given an initial node, it will look for the best move that the current player can perform,
    under the assumption that both players will play rationally (i.e optimally);
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

        for curr_succ in self.problem.get_successors(initial_node):
            self.num_of_visited_states += 1
            # If the maximum depth is set to 0, return a random successor node;
            if self.search_depth == 0:
                self.obtained_successor = random.choice(self.problem.get_successors(initial_node))
                self.obtained_value = self.problem.value(self.obtained_successor)
                break
            
            # A certain player might play more than one turn in a row, 
            # so no assumptions are made with respect to the turn alternation;
            if curr_succ.is_max():
                result = self.__max(curr_succ, curr_depth + 1)
            else:
                result = self.__min(curr_succ, curr_depth + 1)

            # If a new best move was found, save it along with the value provided by the search;
            if (initial_node.is_max() and result > self.obtained_value) or (initial_node.is_min() and result < self.obtained_value):
                self.obtained_value = result
                self.obtained_successor = curr_succ
            elif result == self.obtained_value:
                # If two actions yield the same result, pick a random one; 
                self.obtained_successor = random.choice([self.obtained_successor, curr_succ])
        self.search_performed = True

    def __max(self, node, depth):
        if self.problem.is_end_node(node) or depth >= self.search_depth:
            return self.problem.value(node)
        
        result = self.problem.min_value
        for curr_succ in self.problem.get_successors(node):
            self.num_of_visited_states += 1
            if curr_succ.is_max():
                result = max(result, self.__max(curr_succ, depth + 1))
            else:
                result = max(result, self.__min(curr_succ, depth + 1))         
        return result


    def __min(self, node, depth):
        if self.problem.is_end_node(node) or depth >= self.search_depth:
            return self.problem.value(node)
        
        result = self.problem.max_value
        for curr_succ in self.problem.get_successors(node):
            self.num_of_visited_states += 1
            if curr_succ.is_max():
                result = min(result, self.__max(curr_succ, depth + 1))
            else:
                result = min(result, self.__min(curr_succ, depth + 1))       
        return result

    





