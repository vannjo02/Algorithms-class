import random

class AVLTree:
    
    class AVLNode:
        def __init__(self,item,balance=0,left=None,right=None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance
        
        def check(self):
            lh = depth(self.left)
            rh = depth(self.right)
            balance = rh - lh
            if self.balance != balance:
                print("Not Working",rpr(self))
                raise Exception("Problem")
            if self.left != None:
                self.left.check()
            if self.right != None:
                self.right.check()
        
        def depth(root):
            if root==None:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        
        
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
                            
            yield self.item
                    
            if self.right != None:
                for elem in self.right:
                    yield elem        
        
        
            
        def __repr__(self):
            return "AVLTree.AVLNode("+repr(self.item)+",balance="+repr(self.balance)+",left="+repr(self.left)+",right="+repr(self.right)+")"
        
           
        def rotateLeft(self):
              #  Perform a left rotation of the subtree rooted at the
               #receiver.  Answer the root node of the new subtree.  
              
            child = self.right
            if (child == None):
                print( 'Error!  No right child in rotateLeft.' )
                return None  # redundant
            else:
                self.right = child.left
                child.left = self
                return child
        
        def rotateRight(self):
           #   '''  Perform a right rotation of the subtree rooted at the
            #   receiver.  Answer the root node of the new subtree.  
              
            child = self.left
            if (child == None):
                print( 'Error!  No left child in rotateRight.' )
                return None  # redundant
            else:
                self.left = child.right
                child.right = self
                return child
        
        def rotateRightThenLeft(self):
              #'''Perform a double inside left rotation at the receiver.  We
               #assume the receiver has a right child (the bad child), which has a left 
               #child. We rotate right at the bad child then rotate left at the pivot 
               #node, self. Answer the root node of the new subtree.  We call this 
               #case 3, subcase 2.
              #'''
            pivot = self
            badChild = self.right
            badGrandChild = badChild.left
            badChild.left = badGrandChild.right
            badGrandChild.right = badChild
            self.right = badGrandChild.left
            badGrandChild.left = self
            return badGrandChild
            
            
            #pass
              
        def rotateLeftThenRight(self):
              #'''Perform a double inside right rotation at the receiver.  We
               #assume the receiver has a left child (the bad child) which has a right 
               #child. We rotate left at the bad child, then rotate right at 
               #the pivot, self.  Answer the root node of the new subtree. We call this 
               #case 3, subcase 2.
              #'''
            pivot = self
            badChild = self.left
            badGrandChild = badChild.right
            badChild.right = badGrandChild.left
            badGrandChild.left = badChild
            self.left = badGrandChild
            self.left = badGrandChild.right
            badGrandChild.right = self
            return badGrandChild
            
            #pass        
        
              
        
    def __init__(self,root=None):
        self.root = root
        self.count = 0
    
    def check(self):
        self.root.check()   
        
    def depth(node):
        if node==None:
            return 0
        return 1 + max(depth(node.left), depth(node.right))        
        
    def insert(self, item):
                
        
        def __insert(root,item):
            if root ==None:
                return AVLTree.AVLNode(item)            
            
            if item < root.item:
                root.left=__insert(root.left,item)
                if root.balance == 0 or root.balance == 1:
                    root.balance -= 1
                if root.balance == -1:
                    root.rotateRight
                
                
            if item > root.item:
                root.right=__insert(root.right,item)
                if root.balance == 0 or root.balance == -1:
                    root.balance += 1
                if root.balance == 1:
                    root.rotateLeft
                    
                    
            return root
        
        self.pivotFound = False
        self.root = __insert(self.root,item)
        
    def __repr__(self):
        return "AVLTree(" + repr(self.root) + ")"
    
    def __iter__(self):
        return iter(self.root)
    
    def adjustBalances(self, pivot, item):
          #'''  We adjust the balances of all the nodes in theStack, up to and
           #  including the pivot node, if any.  Later rotations may cause
           #  some of the balances to change.
          #'''
        
        current = self.root
        done = False
        while not done:
            if item > current.item and pivot!=0:
                currrent.balance=current.balance+1
            elif item < current.item and pivot!=0:
                current.balance=current.balance-1
                if current.balance==0:
                    pivot=current
                    break
        
        #pass         
          
    def case1(self, pivot, newItem):
          #'''  There is no pivot node.  Adjust the balances of all the nodes
           #  in theStack.
          #'''
        self.adjustBalances(theStack, pivot, item)
                
    def case2(self, theStack, pivot, newItem):
          #''' The pivot node exists.  We have inserted a new node into the
           #  subtree of the pivot of smaller height.  Hence, we need to adjust 
            # the balances of all the nodes in the stack up to and including 
             #that of the pivot node.  No rotations are needed.
          #'''
        self.adjustBalances(theStack, pivot, newItem)
                
    def case3(self, theStack, pivot, newItem):
        #'''  The pivot node exists.  We have inserted a new node into the
           #  larger height subtree of the pivot node.  Hence rebalancing and 
            # rotations are needed.
          #'''
        self.adjustBalances(theStack, pivot, newItem)
          # Lots more!!!!
             
      
def main():
    print(" My name is Juan")
    print("")
    n = AVLTree()
    for i in range(1000):
        num = random.randrange(1000)
        n.insert(num)
    

    
    print(n)    

if __name__ == '__main__': 
    main()