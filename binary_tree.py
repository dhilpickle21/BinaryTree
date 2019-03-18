"""
An example file for a Binary Tree implementation
in Python
"""

class Node:
    """
    Binary Tree implementationself.  This binary Tree
    contains left, right, value.  left is a reference
    to another Node (lesser value), right is a reference
    to another Node (of greater value), and value is the
    numerical value associated with this Node
    """
    def __init__(self, root_node_value):
        self.left = None
        self.right = None
        self.value = root_node_value

    def add(self, new_value):
        """
        add a new node to the tree
        """
        pass

    def print(self):
        """
        print the entire tree
        """
        pass

    def size(self):
        """
        return the size of the tree, ie., the number of nodes
        """
        return -1