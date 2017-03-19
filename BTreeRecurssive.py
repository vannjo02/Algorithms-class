
    def insert(self,bTree,item):
        '''
        Insert an item in the node. Return three values as a tuple, 
        (left,item,right). If the item fits in the current node, then 
        return self as left and None for item and right. Otherwise, return 
        two new nodes and the item that will separate the two nodes in the parent. 
        '''
        if (self.child[0] == None) and (self.isFull() != True):
            #store item in node
            self.items[self.numberOfKeys] = item
            self.numberOfKeys += 1
            return self, None, None
        elif (self.child[0] == None):
            return self.splitNode(bTree, item, None)

        elif (self.child[0] != None):
            #call insert recursively on appropriate subtree
            newItem = self.appropriateSubtree(bTree, item)
            correctChild = bTree.nodes[newItem]
            newKey = correctChild.insert(bTree, item)
            #take recursive insert and see if there is a newly promoted key and right subtree
            if newKey[2] != None:
                if self.isFull() != True:
                    self.items[self.numberOfKeys]= returnVal[1]
                    self.numberOfKeys += 1 
                    #Change other two children
            else:
                return self.splitNode(bTree, item, newKey[1])

            #if there is, store the new item and subtree pointer in the node.
            #if ther isn't, split again


    def sortFunc(self):
        temp = []
        for i in range(self.numberOfKeys):
            if self.items[i] is not None:
                temp.append(self.items[i])
        temp.sort()
        for i in range(self.numberOfKeys, len(self.items)):
            temp.append(self.items[i])
        self.items = temp

    def appropriateSubtree(self, item):
        foundVariable = False
        i = 0
        while (self.numberOfKeys > i) or (foundVariable == False):
            if item > self.items[i]:
                foundVariable = True
            i += 1 
        if foundVariable == False:
            return self.numberOfKeys
        return i

    def splitNode(self,bTree,item,right):
        '''
        This method is given the item to insert into this node and the node 
        that is to be to the right of the new item once this node is split.
        
        Return the indices of the two nodes and a key with the item added to 
        one of the new nodes. The item is inserted into one of these two 
        nodes and not inserted into its children.
        '''
        #make a new node
        newNode = Btree.getFreeNode()
        #sort
        self.sortFunc()
        #choose middle item to promote to parent
        middle = numberOfKeys//2
        median = self.items[middle]
        #take items after middle and put in new node
        self.items[median:]
        #return tuple of middle item and new right node 
        



    
    def getLeftMost(self,bTree):
        ''' Return the left-most item in the 
            subtree rooted at self.
        '''
        if self.child[0] == None:
            return self.items[0]
        
        return bTree.nodes[self.child[0]].getLeftMost(bTree)

    def delete(self,bTree,item):
        '''
           The delete method returns None if the item is not found
           and a deep copy of the item in the tree if it is found.
           As a side-effect, the tree is updated to delete the item.
        '''
        #If node containing item is a leaf node and node has more than degree items, item may be deleted
        #if (self.child[0] == None) and (self.getNumberOfKeys() > self.degree):
            ##item may be deleted

        ##If node containing item is a leaf node and has degree or fewer items in it before deleting, rebalancing is required
        #elif (self.child[0] == None) and (self. < ):

        ##If node is a non leaf node then the least value of the right subtree can replace the item in the node.
        #elif (self.child[0] != None):

        
    def redistributeOrCoalesce(self,bTree,childIndex):
        '''
          This method is given a node and a childIndex within 
          that node that may need redistribution or coalescing.
          The child needs redistribution or coalescing if the
          number of keys in the child has fallen below the 
          degree of the BTree. If so, then redistribution may
          be possible if the child is a leaf and a sibling has 
          extra items. If redistribution does not work, then 
          the child must be coalesced with either the left 
          or right sibling.

          This method does not return anything, but has the 
          side-effect of redistributing or coalescing
          the child node with a sibling if needed. 
        '''
        pass 


    def getChild(self,i):
        # Answer the index of the ith child
        if (0 <= i <= self.numberOfKeys):
            return self.child[i]
        else:
            print( 'Error in getChild().' )
            
    def setChild(self, i, childIndex):
        # Set the ith child of the node to childIndex
        self.child[i] = childIndex 

    def getIndex(self):
        return self.index

    def setIndex(self, anInteger):
        self.index = anInteger

    def isFull(self):
        ''' Answer True if the receiver is full.  If not, return
          False.
        '''
        return (self.numberOfKeys == len(self.items))

    def getNumberOfKeys(self):
        return self.numberOfKeys

    def setNumberOfKeys(self, anInt ):
        self.numberOfKeys = anInt

    def clear(self):
        self.numberOfKeys = 0
        self.items = [None]*len(self.items)
        self.child = [None]*len(self.child)

    def search(self, bTree, item):
        '''Answer a dictionary satisfying: at 'found'
          either True or False depending upon whether the receiver
          has a matching item;  at 'nodeIndex' the index of
          the matching item within the node; at 'fileIndex' the 
          node's index. nodeIndex and fileIndex are only set if the 
          item is found in the current node. 
        '''
        #if bTree == None:
            #return 0
        #else:
            #if item = bTree.item:
                #return 1
            #else:
                
        #elif target == bTree.
        #searchItem=anItem
        #count=0
        #index=None        
        #found=False
        #while ((not found) and (count<self.numberOfKeys)):
            #if self.items[count]!=searchItem:
                #if self.items[count]> searchItem:
                    #index=count
                    #count=self.numberOfKeys+1
                #else:
                    #count+=1 #for items less than self.items[count], count+1 is the index
            #else:
                #found=True
                #index=count
        #if count==self.numberOfKeys:
            #index=self.numberOfKeys
            
        #searchDict={'nodeIndex':index,'found':found}
        

        ##Recursive
        #if item not in self:
            #return None
        #if self.items[] > item:
            #self.search(self.child[], item)
        #if self.items[] < item:
            #self.search(self.child[], item)
        #searchDict = {'nodeIndex':, 'found':}


        #return searchDict


class BTree:
    def __init__(self, degree, nodes = {}, rootIndex = 1, freeIndex = 2):
        self.degree = degree
        
        if len(nodes) == 0:
            self.rootNode = BTreeNode(degree)
            self.nodes = {}
            self.rootNode.setIndex(rootIndex)
            self.writeAt(1, self.rootNode)  
        else:
            self.nodes = deepcopy(nodes)
            self.rootNode = self.nodes[rootIndex]
              
        self.rootIndex = rootIndex
        self.freeIndex = freeIndex
        
    def __repr__(self):
        return "BTree("+str(self.degree)+",\n "+repr(self.nodes)+","+ \
            str(self.rootIndex)+","+str(self.freeIndex)+")"

    def __str__(self):
        st = '  The degree of the BTree is ' + str(self.degree)+\
             '.\n'
        st += '  The index of the root node is ' + \
              str(self.rootIndex) + '.\n'
        for x in range(1, self.freeIndex):
            node = self.readFrom(x)
            if node.getNumberOfKeys() > 0:
                st += str(node) 
        return st


    def delete(self, anItem):
        ''' Answer None if a matching item is not found.  If found,
          answer the entire item.
        ''' 
        searchTreeDict = self.__searchTree(anItem)
        if (searchTreeDict['found']==False):#if False 
            return None
        return anItem 

    def getFreeIndex(self):
        # Answer a new index and update freeIndex.  Private
        self.freeIndex += 1
        return self.freeIndex - 1

    def getFreeNode(self):
        #Answer a new BTreeNode with its index set correctly.
        #Also, update freeIndex.  Private
        newNode = BTreeNode(self.degree)
        index = self.getFreeIndex()
        newNode.setIndex(index)
        self.writeAt(index,newNode)
        return newNode

    def inorderOn(self, aFile):
        '''
          Print the items of the BTree in inorder on the file 
          aFile.  aFile is open for writing.
        '''
        aFile.write("An inorder traversal of the BTree:\n")
        self.inorderOnFrom( aFile, self.rootIndex)

    def inorderOnFrom(self, aFile, index):
        ''' Print the items of the subtree of the BTree, which is
          rooted at index, in inorder on aFile.
        '''
        currentNode=self.readFrom(index)
        if currentNode!=None:
            for i in range(currentNode.getNumberOfKeys()):
                if currentNode.child[i]!=None:
                    self.inorderOnFrom(aFile,currentNode.child[i])#doing recursion on each node item's child until leafNode is found
                aFile.write(str(currentNode.items[i])+'\n')
            if currentNode.getNumberOfKeys()!=None:#moving to next item in a node
                self.inorderOnFrom(aFile,currentNode.child[currentNode.getNumberOfKeys()])

    def insert(self, anItem):
        ''' Answer None if the BTree already contains a matching
          item. If not, insert a deep copy of anItem and answer
          anItem.
        '''
        searchTreeDict = self.__searchTree(anItem)
        if (searchTreeDict['found']==True):#if True 
            return None
        else:
            newItem = deepcopy(anItem)
            nodeToInsert = self.readFrom(searchTreeDict['fileIndex'])#searchItem ['fileIndex'] give index of a node
            if nodeToInsert.isFull():
                self.splitNode(nodeToInsert,newItem,None,None)
            else:
                nodeToInsert.insertItem(newItem)
                self.writeAt(nodeToInsert.index,nodeToInsert)#inserting into an array of node dict w/ modification
        return anItem  

    def levelByLevel(self, aFile):
        ''' Print the nodes of the BTree level-by-level on aFile. )
        '''
        aFile.write("A level-by-level listing of the nodes:\n")
        queue=MyQueue()
        queue.enqueue(self.rootNode)
        while not queue.isEmpty():
            currentNode=queue.dequeue()
            aFile.write(str(currentNode))
            for i in range(currentNode.getNumberOfKeys()+1):
                child=self.readFrom(currentNode.child[i])
                if child!=None:
                    queue.enqueue(child)

    def readFrom(self, index):
        ''' Answer the node at entry index of the btree structure.
          Later adapt to files
        '''
        if self.nodes.__contains__(index):
            return self.nodes[index]
        else:
            return None

    def recycle(self, aNode):
        # For now, do nothing
        aNode.clear()

    def retrieve(self, anItem):
        ''' If found, answer a deep copy of the matching item.
          If not found, answer None
        '''
        searchTreeDict=self.search(anItem)
        if not searchTreeDict['found']:
            return None
        else:
            item=deepcopy(self.readFrom(searchTreeDict['fileIndex']).items[searchTreeDict['nodeIndex']])
                
        return item

    def __searchTree(self, anItem):
        ''' Answer a dictionary.  If there is a matching item, at
          'found' is True, at 'fileIndex' is the index of the node
          in the BTree with the matching item, and at 'nodeIndex'
          is the index into the node of the matching item.  If not,
          at 'found' is False, but the entry for 'fileIndex' is the
          leaf node where the search terminated.
        '''
        self.nodes.clear()#clearing previously put nodes
        currentNode=self.rootNode
        searchDict=currentNode.search(self, anItem)
        while(not searchDict['found']) and (not currentNode.child[0]==None): #currentNode.child[0]it's not leaf node
            self.nodes.push(currentNode)
            nextSearchNode=currentNode.child[searchDict['nodeIndex']]
            currentNode=self.readFrom(nextSearchNode)
            searchDict=currentNode.searchNode(anItem)
        searchTreeDict={'fileIndex':currentNode.index,'nodeIndex':searchDict['nodeIndex'],'found':searchDict['found']}
        return searchTreeDict  

 
    def update(self, anItem):
        ''' If found, update the item with a matching key to be a
          deep copy of anItem and answer anItem.  If not, answer None.
        '''
        searchTreeDict=self.__searchTree(anItem)
        if not searchTreeDict[----'found']:
            return None
        else:
            node=self.readFrom(searchTreeDict['fileIndex'])
            node.items[searchTreeDict['nodeIndex']]=deepcopy(anItem)
            return anItem
            

    def writeAt(self, index, aNode):
        ''' Set the element in the btree with the given index
          to aNode.  This method must be invoked to make any
          permanent changes to the btree.  We may later change
          this method to work with files.
          This method is complete at this time.
        '''
        self.nodes[index] = aNode

def btreemain():
    print("My name is Joshua Vannatter")

    lst = [10,8,22,14,12,18,2,50,15]
    
    b = BTree(2)
    
    for x in lst:
        print(repr(b))
        print("***Inserting",x)
        b.insert(x)
    
    print(repr(b))
    
    lst = [14,50,8,12,18,2,10,22,15]
    
    for x in lst:
        print("***Deleting",x)
        b.delete(x) 
        print(repr(b))
    
    #return 
    lst = [54,76]
    
    for x in lst:
        print("***Deleting",x)
        b.delete(x)
        print(repr(b))
        
    print("***Inserting 14")
    b.insert(14)
    
    print(repr(b))
    
    print("***Deleting 2")
    b.delete(2)
    
    print(repr(b))
    
    print ("***Deleting 84")
    b.delete(84)
    
    print(repr(b))
    


def readRecord(file,recNum,recSize):
    file.seek(recNum*recSize)
    record = file.read(recSize)
    return record

def readField(record,colTypes,fieldNum):
    # fieldNum is zero based
    # record is a string containing the record
    # colTypes is the types for each of the columns in the record
    
    offset = 0
    for i in range(fieldNum):
        colType = colTypes[i]
        
        if colType == "int":
            offset+=10
        elif colType[:4] == "char":
            size = int(colType[4:])
            offset += size
        elif colType == "float":
            offset+=20
        elif colType == "datetime":
            offset+=24

    colType = colTypes[fieldNum]

    if colType == "int":
        value = record[offset:offset+10].strip()
        if value == "null":
            val = None
        else:
            val = int(value)
    elif colType == "float":
        value = record[offset:offset+20].strip()
        if value == "null":
            val = None
        else:        
            val = float(value)
    elif colType[:4] == "char":
        size = int(colType[4:])
        value = record[offset:offset+size].strip()
        if value == "null":
            val = None
        else:        
            val = value[1:-1] # remove the ' and ' from each end of the string
            if type(val) == bytes:
                val = val.decode("utf-8") 
    elif colType == "datetime":
        value = record[offset:offset+24].strip()
        if value == "null":
            val = None
        else:        
            if type(val) == bytes:
                val = val.decode("utf-8") 
            val = datetime.datetime.strptime(val,'%m/%d/%Y %I:%M:%S %p')
    else:
        print("Unrecognized Type")
        raise Exception("Unrecognized Type") 
    
    return val

class Item:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return "Item("+repr(self.key)+","+repr(self.value)+")"

    def __eq__(self,other):
        if type(self) != type(other):
            return False

        return self.key == other.key
    
    def __lt__(self,other):
        return self.key < other.key
    
    def __gt__(self,other):
        return self.key > other.key
    
    def __ge__(self,other):
        return self.key >= other.key
    
    def getValue(self):
        return self.value
    
    def getKey(self):
        return self.key
            

def main():
    # Select Feed.FeedNum, Feed.Name, FeedAttribType.Name, FeedAttribute.Value where
    # Feed.FeedID = FeedAttribute.FeedID and FeedAttribute.FeedAtribTypeID = FeedAttribType.ID
    attribTypeCols = ["int","char20","char60","int","int","int","int"]
    feedCols = ["int","int","int","char50","datetime","float","float","int","char50","int"]
    feedAttributeCols = ["int","int","float"]
    
    feedAttributeTable = open("FeedAttribute.tbl","r")
    
    if os.path.isfile("Feed.idx"):
        indexFile = open("Feed.idx","r")
        feedTableRecLength = int(indexFile.readline())
        feedIndex = eval("".join(indexFile.readlines()))
    else:
        feedIndex = BTree(3)
        feedTable = open("Feed.tbl","r")
        offset = 0
        for record in feedTable:
            feedID = readField(record,feedCols,0)
            anItem = Item(feedID,offset)
            feedIndex.insert(anItem)
            offset+=1
            feedTableRecLength = len(record)
         
        print("Feed Table Index Created")  
        indexFile = open("Feed.idx","w")
        indexFile.write(str(feedTableRecLength)+"\n")
        indexFile.write(repr(feedIndex)+"\n")
        indexFile.close()
        
    if os.path.isfile("FeedAttribType.idx"):
        indexFile = open("FeedAttribType.idx","r")
        attribTypeTableRecLength = int(indexFile.readline())
        attribTypeIndex = eval("".join(indexFile.readlines()))
    else:
        attribTypeIndex = BTree(3)
        attribTable = open("FeedAttribType.tbl","r")
        offset = 0
        for record in attribTable:
            feedAttribTypeID = readField(record,attribTypeCols,0)
            anItem = Item(feedAttribTypeID,offset)
            attribTypeIndex.insert(anItem)
            offset+=1
            attribTypeTableRecLength = len(record)
         
        print("Attrib Type Table Index Created")
        indexFile = open("FeedAttribType.idx","w")
        indexFile.write(str(attribTypeTableRecLength)+"\n")
        indexFile.write(repr(attribTypeIndex)+"\n")
        indexFile.close()
    
    feedTable = open("Feed.tbl","rb")
    feedAttribTypeTable = open("FeedAttribType.tbl", "rb")
    before = datetime.datetime.now()
    for record in feedAttributeTable:
        
        feedID = readField(record,feedAttributeCols,0)
        feedAttribTypeID = readField(record,feedAttributeCols,1)
        value = readField(record,feedAttributeCols,2)
          
        lookupItem = Item(feedID,None)
        item = feedIndex.retrieve(lookupItem)
        offset = item.getValue()
        feedRecord = readRecord(feedTable,offset,feedTableRecLength)   
        feedNum = readField(feedRecord,feedCols,2)
        feedName = readField(feedRecord,feedCols,3)
        
        lookupItem = Item(feedAttribTypeID,None)
        item = attribTypeIndex.retrieve(lookupItem)
        offset = item.getValue()
        feedAttribTypeRecord = readRecord(feedAttribTypeTable,offset, \
            attribTypeTableRecLength)               
        feedAttribTypeName = readField(feedAttribTypeRecord,attribTypeCols,1)
        
        print(feedNum,feedName,feedAttribTypeName,value)
    after = datetime.datetime.now()
    deltaT = after - before
    milliseconds = deltaT.total_seconds() * 1000    
    print("Done. The total time for the query with indexing was",milliseconds, \
        "milliseconds.")
    
if __name__ == "__main__":
    btreemain()