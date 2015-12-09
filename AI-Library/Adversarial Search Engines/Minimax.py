from AdversarialSearchEngine import AdversarialSearchEngine

class Minimax(AdversarialSearchEngine):
    
    def __init__(self, problem, search_depth = 1):
        super(AdversarialSearchEngine, self).__init__(problem, search_depth)
    
    def perform_search(initial_node):
        
        """
        """
        
        self.obtained_successor = None
        self.obtained_value = self.problem.min_value
        curr_depth = 0

        for curr_succ in self.problem.get_successors(initial_node):
            if self.search_depth == 0:
                self.obtained_value = self.problem.value(initial_node)
                break
                
            if curr_succ.is_max:
                result = __max(curr_succ, curr_depth + 1)
            else:
                result = __min(curr_succ, curr_depth + 1)

            if result > self.obtained_value:
                self.obtained_value = result
                obtained_successor = curr_succ

    def __max(node, depth):
        if self.problem.is_end_node(node) or depth == self.search_depth:
            return self.problem.value(node)
        
        result = self.problem.min_value
        for curr_succ in self.problem.get_successors(node):
            if curr_succ.is_max:
                result = min(result, __max(curr_succ, curr_depth + 1))
            else:
                result = min(result, __min(curr_succ, curr_depth + 1))         
        return result


    def __min(node, depth):
        if self.problem.is_end_node(node) or depth == self.search_depth:
            return self.problem.value(node)
        
        result = self.problem.max_value
        for curr_succ in self.problem.get_successors(node):
            if curr_succ.is_max:
                result = max(result, __max(curr_succ, curr_depth + 1))
            else:
                result = max(result, __min(curr_succ, curr_depth + 1))       
        return result

    





