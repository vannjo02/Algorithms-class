class BinarySearchTree: 
    def __init__(self):
        self.tree = None
        
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def insert(self,val):
        self.tree = __insert(self.tree.val)
    
    def __insert(node,val):
        if node == None: 
            return Node(val)
        if node.getVal() < val:
            node.setRight(__insert(node.getRight(),val))
            return node
        