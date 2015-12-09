from abc import ABCMeta
from abc import abstractmethod

class AdversarialSearchEngine(metaclass= ABCMeta):
    """
    Abstract class which contains the elements necessary to define 
    an adversarial search engine;
    """

    def __init__(self, problem, search_depth = 1):
        self.problem = problem
        self.search_depth = search_depth
        self.search_performed = False
        self.obtained_value = None
        self.obtained_successor = None

    @abstractmethod
    def perform_search(self, initial_node):
        """
        Perform a search from the provided initial state, by using the rules
        expressed in the associated problem;
        """
        return

    def set_search_depth(self, search_depth = 1):
        self.search_depth = search_depth

    def set_problem(self, problem):
        self.problem = problem

    def reset_engine(self):
        """
        Reset the engine, so that a new search can be performed:
        the obtained value and successor are reset, 
        while the search depth and the problem are preserved;
        """
        self.search_performed = False
        self.obtained_successor = False
        self.obtained_value = 0

    
