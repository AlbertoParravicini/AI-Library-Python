from abc import ABCMeta
from abc import abstractmethod


class AdversarialProblem(metaclass=ABCMeta):
    """
    This abstract class represents adversarial search problems,
    and contains the functions required to implement correctly an adversarial search problem;
    It contains a reference to the starting node of the problem, 
    the heuristic evalutation function (if available), the function to calculate 
    the successor of a given node, and the Min/Max values used by the problem;
    """

    def __init__(self):
        self.max_value = None
        self.min_value = None

    @abstractmethod
    def get_successors(self, node):
        """
        Parameters: 
            state: the node of which we want to obtain the successors;
        
        Return: 
            a list containing the successor of the given node; 
            this list can be empty if no successors exist;
        """
        return

    @abstractmethod
    def is_end_node(self, node):
        """
        Parameters: 
            node: the node of which one wants to test whether it is a final node or not;
        
        Returns:
            a boolean value representing whether tyhe given node is final or not;
        """
        return

    @abstractmethod
    def value (self, node):
        """
        Parameters:
            node: a node of which one wants to know an estimated value, 
            i.e. how good the state contained in it is; 

        Returns: an integer value representing how good the node is;
        """
        return

    