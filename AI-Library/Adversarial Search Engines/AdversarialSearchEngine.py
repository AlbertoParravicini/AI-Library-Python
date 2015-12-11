from abc import ABCMeta
from abc import abstractmethod

class AdversarialSearchEngine(metaclass= ABCMeta):
    """
    Abstract class which contains the elements necessary to define 
    an adversarial search engine: the engine can perform a search
    on a given initial node, and will calculate a node which encapsulate the 
    best possible state that the current player can reach (in a single ply)
    from the one on which the search was performed. The calculated node, and its value,
    are stored in the engine and are accessible to the user;
    """

    def __init__(self, problem, search_depth = 1):
        """
        Initialize the engine with the provided parameters:
        note that to perform a search it is necessary to specify a problem 
        with all its abstract funcitions implemented. 
        The default depth of the search is set to 1, meaning that the engine 
        will compute the next node considering only one ply.

        Parameters: 
        -------------
        problem: the problem which will be used by the engine; to perform 
                 a successful search, the problem has to specify all its abstract functions;
        search_depth: the depth of the engine, i.e. the numbers of plies considered by it;      
        """
        self.problem = problem
        self.search_depth = search_depth
        self.search_performed = False
        self.obtained_value = None
        self.obtained_successor = None

    @abstractmethod
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
        return

    def set_search_depth(self, search_depth = 1):
        """
        Set the maximum depth of the search tree; by default it is set to 1, 
        but most problems will require higher values to achieve acceptable results;
        
        Parameters:
        -------------
        search_depth: the new maximum depth of the search tree
        """
        self.search_depth = search_depth

    def set_problem(self, problem):
        """
        Set the problem that should be evaluated by the engine;
        
        Parameters:
        ------------
        problem: the new problem to be evaluated by the engine;
        """
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

    
