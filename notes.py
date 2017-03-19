'''2nd assignment
dijkstra's alg
class priorityqueue:
    #constructor creates a heap 

def enqueue(self, item): 
    
def dequeue(self, item):
        
def isEmpty(self:
            
            
           
Height balanced AVL trees

Balance is maintained in each node
and is called balance. Subtrees are referenced as aleft andright.


Build an AVL tree
Balanceof eery node must be 0, -1, 1.
Balance, (node), is height (right) - height (left)
Empty tree has height 0. A leafe node has height 1.
Values: 50, 75, 85.



Implementation of recursively inserted AVL trees. Remain balance. 

1) two rotations are necessary. Pass to it a root node and return a new root. 
2) Find pivot, add a flag called pivotFound to the AVL tree class. 
    the only reason for teh pivotFound varialbe, is to avoid adjusting balances 
    higher in the tree. 
3) write __insert recursive function 
4) adjust balancees up to pivot node 
5) if we find pivot has -2 or 2 balance, do case 3. 
6) at the end of __insert make sure you return the root node. 

'''

class AVLTree:
    
    def check(self):
        self.root.check()
    
class AVLNode: 
    
    def check(self): 
        compBalance = depth(self.right) - depth(self.left)
        #depth is a recursive function, not a method
    def depth(root):
        if root = None:
            return 0
        return max(depth(root.left), depth(self.right)) 
    
    
'''
11/2/2015
'''

def depth(node): 
    if node==None:
        return 0 
    return 1+ max(depth(node.left), depth(node.right))

AVLNode(item, balance)


# In AVL tree class::
def check(self): 
    self.root.check()
    
#in AVL node class:
def check(self):
    lh = depth(self.left)
    rh = depth(self.right) 
    balance = rh-lh
    if self.balance != balance:
        print(repr(self)) 
        raise Exception("Balance Problem")
    
    
    if self.left != None:
        self.left.check()
    if self.right != None: 
        self.right.check()
        

#Part of AVL Tree class:

def __insert(root,item): 
    if root == None:
        return AVLNode(item) 
    
    if item < root.item: 
        root.left = __insert(root.left, item)
        
    if item > root.item: 
        root.right = __insert(root.right, item)
        
    return root