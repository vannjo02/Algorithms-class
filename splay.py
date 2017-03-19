import datetime
import random
import time


'''
 File: splay.py
 Author: Kent D. Lee
 Date: 8/21/2014
 Description: This module implements the SplayTree class. This
   class uses the SplayNode class.  The classes
   use bottom up splaying rather than top down splaying.  We
   do not allow duplicate objects in the tree.

   Delete is not implemented in this file currently. Test code
   should be added to thoroughly test insert, lookup, and delete. 
   Recall that looking up a value rotates it to the root. Deleting 
   an item rotates its parent to the root. 
'''

def rotateLeft(pivot):
   parent = pivot
   child = parent.right

   parent.right = child.left
   child.left = parent

   return child

def rotateRight(pivot):
   parent = pivot
   child = parent.left

   parent.left = child.right
   child.right = parent

   return child

def rotateRL(pivot):
   grandpa = pivot
   parent = grandpa.right
   child = parent.left

   parent.left = child.right
   grandpa.right = child.left
   child.left = grandpa
   child.right = parent

   return child

def rotateLR(pivot):
   grandpa = pivot
   parent = grandpa.left
   child = parent.right

   parent.right = child.left
   grandpa.left = child.right
   child.left = parent
   child.right = grandpa

   return child

def rotateRR(pivot):
   grandpa = pivot
   parent = grandpa.left
   child = parent.left

   grandpa.left = parent.right
   parent.right = grandpa
   parent.left = child.right
   child.right = parent

   return child

def rotateLL(pivot):
   grandpa = pivot
   parent = grandpa.right
   child = parent.right

   grandpa.right = parent.left
   parent.left = grandpa
   parent.right = child.left
   child.left = parent

   return child

rotate = {}
rotate["RL"] = rotateRL
rotate["LR"] = rotateLR
rotate["RR"] = rotateRR
rotate["LL"] = rotateLL

singleRotate = {}
singleRotate["R"] = rotateRight
singleRotate["L"] = rotateLeft

class SplayTree:

   class SplayNode:
      def __init__(self, item, left=None, right=None):
         self.item = item
         self.left = left
         self.right = right

      def __str__(self):
         st = '('
         if (self.left == None):
            st += '*'
         else:
            st += str(self.left)
         st += str(self.item)
         if (self.right == None):
            st += '*'
         else:
            st += str(self.right)
         st += ')'
         return st

   def __init__(self):
      self.root = None
      self.rString = ""


   # Pass searching = True if just searching and not 
   # really inserting. If the item is found, true is 
   # returned. If the item is not found, an exception
   # containing false is raised. 

   def insert(self,item,searching=False):

      def __insert(root,item):
         ''' return the new root after inserting
             item into the tree currently rooted at 
             root. If searching for the value and not 
             inserting, then raise Exception(False) if 
             the item is not found. 
         '''
         if root==None and not searching:
            root = SplayTree.SplayNode(item)

         if root==None and searching:
            raise Exception(False)

         if item > root.item:
            root.right = __insert(root.right,item)
            self.rString += "L"

         if item < root.item:
            root.left = __insert(root.left,item)
            self.rString += "R"

         if item == root.item:
            self.found = True

         if self.rString in rotate:
            root = rotate[self.rString](root)
            self.rString = ""

         return root

      self.found = False

      self.root = __insert(self.root,item)

      # Handle any single rotation that must 
      # be done after inserting the value. 
      if self.rString in singleRotate:
         self.root = singleRotate[self.rString](self.root)

      self.rString = ""

      return self.found

   def lookup(self,item):

      try:
         return self.insert(item,True)
      except Exception as inst:
         if inst.args[0] == False:
            return False

         raise Exception(inst)

   def __str__(self):
      if self.root != None:
         return str(self.root)
      else:
         return ""

def main():
   
   xmin = 0
   xmax = 5000
   
   
   file = open("AVLvsSplay.xml","w")
   
   file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
   
   file.write('<Plot title="AVL vs. Splay trees">\n')   
   


   xList=[]
   yList=[] 
   
   
   
   
   tree = SplayTree()
   lines = open("randomsample.txt").read().splitlines()
   count = 0
   
   for line in range(0, len(lines), 20):
      if lines[line][0] == "I":
         
         count += 1
         xList.append(count)   
         
         
         starttime = datetime.datetime.now()         
      
         tree.insert(lines[line][2:])
         
         endtime = datetime.datetime.now()
   
         deltaT = endtime - starttime
         accessTime = deltaT.total_seconds() * 10000000
         yList.append(accessTime)
         
      else:
         
         starttime = datetime.datetime.now()
         
         tree.lookup(lines[line][2:])
         
         endtime = datetime.datetime.now()
                  
         deltaT = endtime - starttime
         accessTime = deltaT.total_seconds() * 10000000   
         yList.append(accessTime)
         
   file.write('  <Axes>\n')
   file.write('    <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">Tree Size</XAxis>\n')
   file.write('    <YAxis min="'+str(min(yList))+'" max="'+str(max(yList))+'">Microseconds</YAxis>\n')
   file.write('  </Axes>\n')

   file.write('  <Sequence title="Tree Comparison" color="red">\n')

   for i in range(len(xList)):
      file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')

   file.write('  </Sequence>\n')

   file.write('</Plot>\n')
   file.close()   


   
if __name__ == '__main__': main()