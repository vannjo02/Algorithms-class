from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime
import time
import sys

class HashMap:
    class __KVPair:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            
        def __eq__(self,other):
            if type(self) != type(other):
                return False
            
            return self.key == other.key
        
        def getKey(self):
            return self.key
        
        def getValue(self):
            return self.value
        
        def __hash__(self):
            return hash(self.key)        
        
    def __init__(self):
        self.hSet = HashSet()
        
    def __len__(self):
        return len(self.hSet)
    
    def __contains__(self,item):
        return HashMap.__KVPair(item,None) in self.hSet
    
    def not__contains__(self,item):
        return item not in self.hSet
    
    def __setitem__(self,key,value):
        self.hSet.add(HashMap.__KVPair(key,value))
        
    def __getitem__(self,key):
        if HashMap.__KVPair(key,None) in self.hSet:
            val = self.hSet[HashMap.__KVPair(key,None)].getValue()
            return val

        raise KeyError("Key " + str(key) + " not in HashMap")        
    
    def get(self,key,default=None):
        if HashMap.__KVPair(key,None) in self.hSet:
            return self.hSet[HashMap.__KVPair(key,None)].getValue()
        else:
            return default
        
    def __delitem__(self,key):
        if HashMap.__KVPair(key,None) in self.hSet:
            self.hSet.remove(key)
        else:
            raise KeyError("Key " + key + " not in HashMap")
        
    def items(self):
        result = []
        for x in self.hSet:
            result.append((x.getKey(),x.getValue()))
        return result
    
    def keys(self):
        result = []
        for x in self.hSet:
            result.append(x.getKey())
        return result    
    
    def values(self):
        result = []
        for x in self.hSet:
            result.append(x.getValue())
        return result   
    
    def pop(self, key):
        if HashMap.__KVPair(key,None) in self.hSet:
            item = self.hSet[key]   
            return item.getValue()
        else:
            raise KeyError("Key " + key + " not in HashMap")
        
    def popitem(self):
        item = self.hSet.pop()
        return (item.getKey(),item.getValue())
    
    def setdefault(self):
        pass
    
    def update(self,other):
        for item in other: 
            if item not in self:
                self.hset.add(item)
            else:
                self.hset.remove(item)
                slef.hset.add(item)
    
    def clear(self):
        pass
    
    def copy(self):
        pass
    
    def __iter__(self):
        for x in self.hSet:
            yield x.getKey()
            
            

class HashSet:
    class __Placeholder:
        def __init__(self):
            pass
        
        def __eq__(self,other):
            return False
        
    def __add(item,items):
        idx = hash(item) % len(items)
        loc = -1
        
        while items[idx] != None:
            if items[idx] == item:
                # item already in set
                return False
            
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx
                
            idx = (idx + 1) % len(items)
            
        if loc < 0:
            loc = idx
            
        items[loc] = item  
        
        return True
    
    def __remove(item,items):
        idx = hash(item) % len(items)
        
        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True
            
            idx = (idx + 1) % len(items)
            
        return False
        
    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newList)
                
        return newList
    
    def __init__(self,contents=[]):
        self.items = [None] * 10
        self.numItems = 0
        
        for item in contents:
            self.add(item)
          
    def __str__(self):
        pass
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]    
    
    # Following are the mutator set methods 
    def add(self, item):
        if HashSet.__add(item,self.items):
            self.numItems += 1             
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))
    def remove(self, item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items,[None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")
        
    def discard(self, item):
        pass
        
    def pop(self):
        pass
            
    def clear(self):
        pass
        
    def update(self, other):
        pass
            
    def intersection_update(self, other):
        pass
            
    def difference_update(self, other):
        for item in other:
            self.discard(item)
                
    def symmetric_difference_update(self, other):
        pass
                
    # Following are the accessor methods for the HashSet  
    def __len__(self):
        pass
    
    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True
            
            idx = (idx + 1) % len(self.items)
            
        return False
    
    # One extra method for use with the HashMap class. This method is not needed in the 
    # HashSet implementation, but it is used by the HashMap implementation. 
    def __getitem__(self, item):
        for x in self.item:
            if item == x:
                return x
        
    def not__contains__(self, item):
        pass
    
    def isdisjoint(self, other):
        pass
    
    
    def issubset(self, other):
        pass
            
    
    def issuperset(self, other):
        pass
    
    def union(self, other):
        pass
    
    def intersection(self, other):
        pass
    #done
    def difference(self, other):
        pass
    
    def symmetric_difference(self, other):
        pass
    
    def copy(self):
        pass
    
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
        pass
    

screenMin = 0
screenMax = 300
Human = -1
Computer = 1  

memo = HashMap()

class Board:
    # When a board is constructed, you may want to make a copy of the board.
    # This can be a shallow copy of the board because Turtle objects are 
    # Immutable from the perspective of a board object. 
    def __init__(self, board=None, screen=None):
        self.screen = screen
        if screen == None: 
            if board!=None:
                self.screen = board.screen

        self.items = []
        for i in range(3):
            rowlst = []
            for j in range(3):
                if board==None:
                    rowlst.append(Dummy())
                else:
                    rowlst.append(board[i][j])

            self.items.append(rowlst)

    # Accessor method for the screen
    def getscreen(self):
        return self.screen

    # The getitem method is used to index into the board. It should 
    # return a row of the board. That row itself is indexable (it is just 
    # a list) so accessing a row and column in the board can be written
    # board[row][column] because of this method.
    def __getitem__(self,index):
        return self.items[index]

    # This method should return true if the two boards, self and other,
    # represent exactly the same state. 
    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
    def __eq__(self,other):
        if type(self) != type(other):
            return False
        for i in range(3):
            for j in range(3):
                if self[i][j].eval() == other[i][j].eval():
                    return True
                return False
            
            
    def __hash__(self):
        val = 0 
        for i in range(3):
            for j in range(3):
                val = val * 3 + self[i][j].eval()+1
        return val

    # This method will mutate this board to contain all dummy 
    # turtles. This way the board can be reset when a new game
    # is selected. It should NOT be used except when starting
    # a new game. 
    def reset(self):

        self.screen.tracer(1)
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100,-100)
                self.items[i][j] = Dummy()

        self.screen.tracer(0)

    # This method should return an integer representing the 
    # state of the board. If the computer has won, return 1.
    # If the human has won, return -1. Otherwise, return 0.
    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
    def eval(self):
        for i in range(3): 
            rowSum = 0 
            colSum = 0
            for j in range(3):
                rowSum += self.items[i][j].eval()
                colSum += self.items[j][i].eval()
            
                if abs(rowSum == 3):
                    return rowSum // 3
                if abs(colSum) == 3:
                    return colSum // 3
            diag1Sum = 0    
            diag2Sum = 0
        for i in range(3):
            diag1Sum += self.items[i][i].eval()
            diag2Sum += self.items[i][2-i].eval()
        
            if abs(diag1Sum) == 3:
                return diag1Sum // 3
            if abs(diag2Sum) == 3:
                return diag2Sum // 3    
            return 0
        
        
       
    

    # This method should return True if the board 
    # is completely filled up (no dummy turtles). 
    # Otherwise, it should return False.
    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
    def full(self): 
        for i in range(3): 
            for j in range(3): 
                if self.items[i][j].eval() == 0:
                    return False
        return True

    # This method should draw the X's and O's
    # Of this board on the screen. 
    def drawXOs(self):

        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(col*100+50,row*100+50)

        self.screen.update()        

# This class is just for placeholder objects when no move has been made
# yet at a position in the board. Having eval() return 0 is convenient when no
# move has been made. 
class Dummy:
    def __init__(self):
        pass

    def eval(self):
        return 0

    def goto(self,x,y):
        pass

# In the X and O classes below the constructor begins by initializing the 
# RawTurtle part of the object with the call to super().__init__(canvas). The
# super() call returns the class of the superclass (the class above the X or O
# in the class hierarchy). In this case, the superclass is RawTurtle. Then, 
# calling __init__ on the superclass initializes the part of the object that is
# a RawTurtle. 
class X(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.getscreen().register_shape("X",((-40,-36),(-40,-44),(0,-4),(40,-44),(40,-36), \
                                             (4,0),(40,36),(40,44),(0,4),(-40,44),(-40,36),(-4,0),(-40,-36)))
        self.shape("X")
        self.penup()
        self.speed(5)
        self.goto(-100,-100)  

    def eval(self):
        return Computer

class O(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.shape("circle")
        self.penup()
        self.speed(5)
        self.goto(-100,-100)

    def eval(self):
        return Human

# The minimax function is given a player (1 = Computer, -1 = Human) and a
# board object. When the player = Computer, minimax returns the maximum 
# value of all possible moves that the Computer could make. When the player =
# Human then minimax returns the minimum value of all possible moves the Human
# could make. Minimax works by assuming that at each move the Computer will pick
# its best move and the Human will pick its best move. It does this by making a 
# move for the player whose turn it is, and then recursively calling minimax. 
# The base case results when, given the state of the board, someone has won or 
# the board is full.    
# READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION



def minimax(player,board, cv):
    
    
    
    if board in memo:
        return memo[board]
    
    val = board.eval()
    if val != 0:
        return val
    
    if board.full(): 
            return 0    
    if player == Computer:
    
        maxMove = -1
    
        for i in range(3):
            for j in range(3): 
                if board[i][j].eval() == 0: 
                    board[i][j] = X(cv)
                    val = minimax(Human, board, cv)
                    memo[hash(board)] = val
                    board[i][j] = Dummy()
                    if val > maxMove:
                        maxMove = val 
        return maxMove
    
    else:
        minMove = 1
        for i in range(3):
            for j in range(3): 
                if board[i][j].eval() == 0: 
                    board[i][j] = X(cv)
                    val = minimax(Human, board, cv)
                    memo[hash(board)] = val
                    board[i][j] = Dummy()
                    if val < minMove:
                        minMove = val
        return minMove
                            


class TicTacToe(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()    
        self.paused = False
        self.stop = False
        self.running = False
        self.turn = Human
        self.locked = False

    def buildWindow(self):

        cv = ScrolledCanvas(self,600,600,600,600)
        cv.pack(side = tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)

        screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
        screen.bgcolor("white")
        t.ht()

        frame = tkinter.Frame(self)
        frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
        board = Board(None, screen)

        def drawGrid():
            screen.clear()
            screen.tracer(1000000)
            screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
            screen.bgcolor("white")
            screen.tracer(0)
            t = RawTurtle(cv)
            t.ht()
            t.pu()
            t.width(10)
            t.color("green")
            for i in range(2):
                t.penup()
                t.goto(i*100+100,10)
                t.pendown()
                t.goto(i*100+100,290)
                t.penup()
                t.goto(10,i*100+100)
                t.pendown()
                t.goto(290,i*100+100)

            screen.update()


        def newGame():
            #drawGrid()
            self.turn = Human
            board.reset()
            self.locked =False
            screen.update()


        def startHandler():
            newGame()

        drawGrid()

        startButton = tkinter.Button(frame, text = "New Game", command=startHandler)
        startButton.pack()  

        def quitHandler():
            self.master.quit()

        quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
        quitButton.pack()

        def computerTurn():
            # The locked variable prevents another event from being 
            # processed while the computer is making up its mind. 
            self.locked = True
            
            maxVal = -1
            for row in range(3):
                for col in range(3): 
                    if board[row][col].eval() == 0: 
                        board[row][col] = X(cv)
                        val = minimax(Human, board, cv)
                        board[row][col] = Dummy()
                        if val > maxVal:
                            maxMove = val 
                            maxMove=(row,col)
                            
                                        
            # Call Minimax to find the best move to make.
            # READER EXERCISE: YOU MUST COMPLETE THIS CODE
            # After writing this code, the maxMove tuple should
            # contain the best move for the computer. For instance,
            # if the best move is in the first row and third column
            # then maxMove would be (0,2).

            row, col = maxMove
            board[row][col] = X(cv)
            self.locked = False


        def mouseClick(x,y):
            if not self.locked:
                row = int(y // 100)
                col = int(x // 100)

                if board[row][col].eval() == 0:
                    board[row][col] = O(cv) 

                    self.turn = Computer

                    board.drawXOs()

                    if not board.full() and not abs(board.eval())==1:
                        computerTurn()

                        self.turn = Human

                        board.drawXOs()
                    else:
                        self.locked = True

                    if board.eval() == 1:
                        tkinter.messagebox.showwarning("Game Over","X wins!!!")

                    if board.eval() == -1:
                        tkinter.messagebox.showwarning("Game Over","O wins. How did that happen?")

                    if board.full():
                        tkinter.messagebox.showwarning("Game Over","It was a tie.")

        screen.onclick(mouseClick)

        screen.listen()

def main():
    root = tkinter.Tk()
    root.title("Tic Tac Toe")    
    application = TicTacToe(root)  
    application.mainloop()

if __name__ == "__main__":
    main()