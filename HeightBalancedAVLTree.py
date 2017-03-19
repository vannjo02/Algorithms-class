'''  
Height balanced AVL trees
-------------------------
Balance is maintained in each node is called balance. Subtress are referenced as left and right.


Build on AVL tree
------------------
Balance of eveery node must be 0, -1, 1.
Balance(node) is height(right)-height(left) 

Empty tree has height 0.  A leaf node has height 1. 


See written notes for example.
----------
can be a standalone function
def depth(node):
     if node == None:
          return 0
          return 1 + max(depth(node.left), depth(node.right))
----------
In AVL Tree Class

def check(self):
     self.root.check()
----------
in AVLNode Class
def check(self):
     leftHeight = depth(self.left)
     rightHeight = depth(self.right)
     balance = rightHeight - leftHeight (not the balance in node)
     
     if self.balance =! balance:
          print(repr(self))
          raise Exception ("balance Problem")
     if self.left != None:
          self.left.check()
     if self.right  != None:
          self.right.check()
------------
part of AVLTree Class
def insert(self, item):

     def __insert(root, item):
          if root == None:
               return AVLNode(item)
               
          if item < root.item:
               root.left = __insert(root.left, item)
               ###FIND PIVOT HERE###
          if item > root.item:
               root.right = __ insert(root.right, item)
               ###FIND PIVOT HERE###
          return root
          
     self.pivotFound = False
     self.root = __insert(self.root,item) 
     
     






'''