'''
Splay trees:
amortized O(logn)
'''
def RR(pivot):
    pass
def RL(pivot):
    pass
def LR(pivot):
    pass
def LL(pivot):
    pass
def left(pivot):
    pass
def right(pivot):
    pass

rotation = {}
rotation["LR"]=LR
rotation["RL"]=RL

if rotationString in rotation:
    rotation[rotationString](pivot)
    
class SplayTree:
    def __repr__(self):
        return "SplayTree("+ repr(self.root) ")"

class SplayNode:
    def __repr__(self):
        return 'SplayNode(' + repr(item + ',' + repr(self.left) + ',' + repr(self.right) + ')'
                                  
        