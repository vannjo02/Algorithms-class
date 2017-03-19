import random
class Stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getElements(self):
        return self.items




class OrderedTreeSet:
    class BinarySearchTree:
        
        
        # This is a Node class that is internal to the BinarySearchTree class. 
        class Node:
            
           


            def __init__(self,val,left=None,right=None):
                self.val = val
                self.left = left
                self.right = right
                
            def getVal(self):
                return self.val
            
            def setVal(self,newval):
                self.val = newval
                
            def getLeft(self):
                return self.left
            
            def getRight(self):
                return self.right
            
            def setLeft(self,newleft):
                self.left = newleft
                
            def setRight(self,newright):
                self.right = newright
                
          
            def __iter__(self):  
                
                if self.left != None:
                    for elem in self.left:
                        yield elem
                
                    yield self.val
                
                    if self.right != None:
                        for elem in self.right:
                            yield elem                

              
                

            def __repr__(self):
                return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
                
        # Below are the methods of the BinarySearchTree class. 
        def __init__(self, root=None):
            self.root = root
            
        def getRightMost(node):
            if node.getRight() == None:
                return node.getVal()
            
            return OrderedTreeSet.BinarySearchTree.getRightMost(node.getRight())
            
        def insert(self,val):
            self.root = OrderedTreeSet.BinarySearchTree.__insert(self.root,val)
            
        def __insert(root,val):
            if root == None:
                return OrderedTreeSet.BinarySearchTree.Node(val)
            
            if val < root.getVal():
                root.setLeft(OrderedTreeSet.BinarySearchTree.__insert(root.getLeft(),val))
            else:
                root.setRight(OrderedTreeSet.BinarySearchTree.__insert(root.getRight(),val))
                
            return root
        
        def delete(self,val):
            self.root = OrderedTreeSet.BinarySearchTree.__delete(self.root,val)

       
        def __delete(root,val):
            if root == None:
                return None

            if val == root.getVal():
                if root.getLeft() == None and root.getRight() == None:
                    return None

                if root.getRight() == None:
                    return root.getLeft()

                if root.getLeft() == None:
                    return root.getRight()

                rm = OrderedTreeSet.BinarySearchTree.getRightMost(root.getLeft())
                root.setVal(rm)
                root.setLeft(OrderedTreeSet.BinarySearchTree.__delete(root.getLeft(),rm))



            elif val < root.getVal():
                root.setLeft(OrderedTreeSet.BinarySearchTree.__delete(root.getLeft(),val))
            else:
                root.setRight(OrderedTreeSet.BinarySearchTree.__delete(root.getRight(),val))

            return root
            
        def __iter__(self):
            
            s=Stack()
            node = OrderedTreeSet.BinarySearchTree.getVal()
            while not s.isEmpty() or node != None:
                if node != None:
                    s.push(node)
                    node = node.getLeft()
                else:
                    node = s.pop()
                    yield node.getVal()
                    node = node.getRight()
            
            #if self.root != None:
             #   return iter(self.root)
            #else:
             #   return iter([])

        def __str__(self):
            return "BinarySearchTree(" + repr(self.root) + ")"
            
    def __init__(self,contents=None):
        self.tree = OrderedTreeSet.BinarySearchTree()
        if contents != None:
            indices = list(range(len(contents)))
            random.shuffle(indices)
            
            for i in range(len(contents)):
                self.tree.insert(contents[indices[i]])
                
            self.numItems = len(contents)
        else:
            self.numItems = 0
            
    def __str__(self):
        pass
    
    def __iter__(self):
        return iter(self.tree)
    
    # Following are the mutator set methods 
    def add(self, item):
        self.numItems+= 1
        self.tree.insert(item)
                
    def remove(self, item):
        if item in self:
            self.numItems = self.numItems - 1
            self.tree.delete(item)
            
        else:
            raise KeyError("Item not found")
        
    def discard(self, item):
        if item in self:
            self.numItems = self.numItems - 1
            self.tree.delete(item)
        
    def pop(self):
        pass
            
    def clear(self):
            
        self.tree = OrderedTreeSet.BinarySearchTree()
        self.numItems = 0
        
    def update(self, other):
        for item in other:
            if item not in self:
                self.add(item)
            
    def intersection_update(self, other):
        temp = []
        for item in self:
            temp.append(item)
        for item in temp:
            if item not in other:
                self.discard(item)
            
    def difference_update(self, other):
        temp = []
        for item in self:
            temp.append(item)
        for item in temp:
            if item in other:
                self.discard(item)
                
    def symmetric_difference_update(self, other):
        pass
                
    # Following are the accessor methods for the HashSet  
    def __len__(self):
        return self.numItems
    
    def __contains__(self, item):
        if item in self.tree:
            return True
        
        return False
    
    # One extra method for use with the HashMap class. This method is not needed in the 
    # HashSet implementation, but it is used by the HashMap implementation. 
    def __getitem__(self, item):
        pass      
        
    def not__contains__(self, item):
        if item not in self.tree:
            return True
        
        return False
    
    def isdisjoint(self, other):
        pass
    
    
    def issubset(self, other):
        for item in self:
            if item not in other:
                return False
        return True
            
    
    def issuperset(self, other):
        for item in other:
            if item not in self:
                return False
            
        return True
    
    def union(self, other):
        pass
    
    def intersection(self, other):
        pass
    def difference(self, other):
        newTree = OrderedTreeSet()
        
        for item in self:
            if item not in other:
                newTree.add(item)
                
        return newTree
    
    def symmetric_difference(self, other):
        pass
    
    def copy(self):
        newTree = OrderedTreeSet()
        
        for item in self:
            newTree.add(item)
            
        return newTree
    
    # Operator Definitions
    def __or__(self, other):
        pass
    
    def __and__(self,other):
        pass
    
    def __sub__(self,other):
        pass
    
    def __xor__(self,other):
        pass
    
    def __ior__(self,other):
        pass
    
    def __iand__(self,other):
        pass
    
    def __ixor(self,other):
        pass    
    
    def __le__(self,other):
        pass
    
    def __lt__(self,other):
        pass
    
    def __ge__(self,other):
        pass
    
    def __gt__(self,other):
        pass
    
    def __eq__(self,other):
        if self.issubset(other) == True and other.issubset(self) == True:
            return True
        
        return False
                
            
    
 
def main():
    lst = []
    lst.append(5)
    lst.append(7)
    lst.append(9)
    lst.append(3)
        
    tree = OrderedTreeSet()
    
    for x in lst:
        tree.add(float(x))
        
    for x in tree:
        print(x)
        
    print(len(tree))
    
    print(tree.tree)
        
    tree.discard(float(5))
    
    print(len(tree))
    
    print(tree.tree)
        
    for x  in tree:
        print(x)
        
    tree.clear()
    
    print(tree.tree)
    a = 101
    b = 99
    
    if a in tree:
        print("Yes, A")
    if b in tree:
        print("Yes, B")

if __name__ == "__main__":
    main()