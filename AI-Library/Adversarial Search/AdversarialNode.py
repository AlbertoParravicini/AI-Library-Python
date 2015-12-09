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
        self.state = state
        self.parent_node = parent_node
        self.rule_applied = rule_applied


    @abstractmethod
    def set_state(self, state):
        return

    @abstractmethod
    def set_parent(self, parent):
        return

    @abstractmethod
    def set_rule_applied(self, rule_applied):
        return

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
