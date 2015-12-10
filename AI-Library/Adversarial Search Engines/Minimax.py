from AdversarialSearchEngine import AdversarialSearchEngine
import random as random

class Minimax(AdversarialSearchEngine):
    
    def __init__(self, problem, search_depth = 1):
        super().__init__(problem, search_depth)
    
    def perform_search(self, initial_node):
        
        """
        """
        
        self.obtained_successor = None
        self.obtained_value = self.problem.min_value if initial_node.is_max() else self.problem.max_value
        curr_depth = 0

        for curr_succ in self.problem.get_successors(initial_node):
            if self.search_depth == 0:
                self.obtained_successor = random.choice(self.problem.get_successors(initial_node))
                self.obtained_value = self.problem.value(self.obtained_successor)
                break
            if curr_succ.is_max():
                result = self.__max(curr_succ, curr_depth + 1)
            else:
                result = self.__min(curr_succ, curr_depth + 1)

            if (initial_node.is_max() and result > self.obtained_value) or (initial_node.is_min() and result < self.obtained_value):
                self.obtained_value = result
                self.obtained_successor = curr_succ
        self.search_performed = True

    def __max(self, node, depth):
        if self.problem.is_end_node(node) or depth == self.search_depth:
            return self.problem.value(node)
        
        result = self.problem.min_value
        for curr_succ in self.problem.get_successors(node):
            if curr_succ.is_max():
                result = max(result, self.__max(curr_succ, depth + 1))
            else:
                result = max(result, self.__min(curr_succ, depth + 1))         
        return result


    def __min(self, node, depth):
        if self.problem.is_end_node(node) or depth == self.search_depth:
            return self.problem.value(node)
        
        result = self.problem.max_value
        for curr_succ in self.problem.get_successors(node):
            if curr_succ.is_max():
                result = min(result, self.__max(curr_succ, depth + 1))
            else:
                result = min(result, self.__min(curr_succ, depth + 1))       
        return result

    





