from xml.dom import minidom
import turtle

class Vertex:
    def __init__(self,vertexId,x,y,label):
        self.vertexId = vertexId
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = []
        self.previous = None
        self.cost = None
        
    def addAdjacent(self,other):
        self.adjacent.append(other)
    
    def getLabel(self):
        return self.label

    def getId(self):
        return self.vertexId

    def getAdjacent(self):
        return self.adjacent

    def setCost(self,aCost):
        self.cost = aCost

    def getCost(self):
        return self.cost

    def setPrevious(self,newPrevious):
        self.previous = newPrevious

    def __eq__(self,other):
        if int(self.label)==int(other.label):
            return True

        return False

    def __ne__(self,other):
        if int(self.label) != int(other.label):
            return True

        return False

    def __lt__(self,other):
        if int(self.label) < int(other.label):
            return True

        return False

    def __le__(self,other):
        if int(self.label) < int(other.label) or int(self.label) == int(other.label):
            return True

        return False

    def __gt__(self,other):
        if int(self.label) > int(other.label):
            return True

        return False

    def __ge__(self,other):
        if int(self.label) > int(other.label) or int(self.label) == int(other.label):
            return True

        return False

    def __str__(self):
        return "Vertex: \n   label: " + self.label + "\n   cost: " + str(round(self.cost,2)) + "\n   previous: " + str(self.previous) + "\n"    
    
    
    
class Edge:
    def __init__(self,v1,v2,weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    def __lt__(self,other):
        return self.weight < other.weight    
        
    def getV1(self):
        return self.v1
    
    def getV2(self):
        return self.v2

    def getWeight(self):
        return self.weight  
    
    
    
def main():
    xmldoc = minidom.parse("graph.xml")
    
    graph = xmldoc.getElementsByTagName("Graph")[0]
    vertices = graph.getElementsByTagName("Vertices")[0].getElementsByTagName("Vertex")
    edges = graph.getElementsByTagName("Edges")[0].getElementsByTagName("Edge")
    
    width = float(graph.attributes["width"].value)
    height = float(graph.attributes["height"].value)
    
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.setworldcoordinates(0,height,width,0)
    t.speed(100)
    t.ht()
    vertexDict = {}
    
    for vertex in vertices:
        vertexId = int(vertex.attributes["vertexId"].value)
        x = float(vertex.attributes["x"].value)
        y = float(vertex.attributes["y"].value)
        label = vertex.attributes["label"].value
        v = Vertex(vertexId, x, y, label)
        vertexDict[vertexId] = v
        print("added", label)
        
    edgeList = []
    
    for edge in edges:
        anEdge = Edge(int(edge.attributes["head"].value), int(edge.attributes["tail"].value))
        if "weight" in edge.attributes:       
            anEdge.weight = float(edge.attributes["weight"].value) 
        edgeList.append(anEdge)
    
    for edge in edgeList:
        x1 = float(vertexDict[edge.v1].x)
        y1 = float(vertexDict[edge.v1].y)
        x2 = float(vertexDict[edge.v2].x)
        y2 = float(vertexDict[edge.v2].y)
        t.penup()
        t.goto(x1,y1)
        t.pendown()
        t.goto(x2,y2)
        if edge.weight != 0:       
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            t.penup()
            t.goto(x,y)
            t.write(str(edge.weight),align="center",font=("Arial",12,"normal"))
                      

    
    for vertexId in vertexDict:
        vertex = vertexDict[vertexId]
        x = vertex.x
        y = vertex.y
        t.penup()
        t.goto(x,y-20)
        
        t.pendown()
        t.fillcolor(0.8,1,0.4)
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.penup()
        t.goto(x+2,y+11)
        t.write(vertex.label,align="center",font=("Arial",12,"bold"))

        
        
        
    screen.exitonclick()
    
if __name__ == "__main__":
    main()
        
    
    