from abc import ABCMeta
from abc import abstractmethod
from AdversarialGameState import AdversarialGameState

class AdversarialNode(metaclass=ABCMeta):
    """
    An adversarial node contains a game state (i.e. a representation of the game),
    a rule (i.e. a representation of the action that lead in the current state),
    and the parent of the current state (i.e. the state from which this state was created);
    """
    
    def __init__(self, state = None, parent_node = None, rule_applied = None):
        """
        Initializes the node with the provided values;
        Each node excepth the first one should have a parent node and a rule, 
        as it should be possible to trace back the sequence of moves that lead to the node;

        Parameters:
        -------------
        state: the state contained in the node;
        parent_node: the node from which this node was generated;
        rule_applied: a representation of the move that lead to this node;
        """
        self.state = state
        self.parent_node = parent_node
        self.rule_applied = rule_applied

   
    def set_state(self, state):
        """
        Sets the state associated to this node;
        
        Parameters:
        -------------
        state: the state contained in the node;
        """
        self.state = state

  
    def set_parent(self, parent_node):
        """
        Sets the parent node associated to this node;
        
        Parameters:
        -------------
        parent_node: the node from which this node was generated;
        """
        self.set_parent = parent_node


    def set_rule_applied(self, rule_applied):
        """
        Sets the rule associated to this node;
        
        Parameters:
        -------------
        rule_applied: a representation of the move that lead to this node;
        """
        self.rule_applied = set_rule_applied

    @abstractmethod
    def is_max(self):
        """
        Returns:
            A boolean value representing if this state is a "Max" node;
        """
        return

    @abstractmethod
    def is_min(self):
        """
        Returns:
            A boolean value representing if this state is a "Min" node;
        """
        return

    def __eq__(self, other_node):
        """
        Checks if two nodes are equal by comparing their respective states;
        
        Returns
            A boolean value representing if self.state is equal to other_node.state;
        """
        return self.state == other_node.state
