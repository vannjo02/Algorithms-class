#On my computer, the comparison time increased like a set of stairs.
#This should not happen, however, on other computers my file created a normal looking graph. 
#I'm still uncertain why my graph looks like stairs instead of a straight line when run on my computer. 






import datetime
import random
import time

def main():

    # Write an XML file with the results
    file = open("stringcomparison.xml","w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    file.write('<Plot title="String Comparison">\n')

    
    xmin = 1000
    xmax = 50000

    xList=[]
    yList=[]
    
    word1 = "o"
    word2 = "o"
    for x in range(xmin, xmax+1, 1000):
        
        xList.append(x)
        
        word1 = word1 + ("t"*1000)
        word2 = word2 + ("t"*1000)
        
        
        
        time.sleep(1)

        # Time before the 1000 test retrievals
        starttime = datetime.datetime.now()

        for i in range(1000):
            if word1 == word2:
                z = word1 == word2
         
        # Time after the 1000 test retrievals
        endtime = datetime.datetime.now()
        print(x,z) 

        # The difference in time between start and end.
        deltaT = endtime - starttime

        # Divide by 1000 for the average access time
        # But also multiply by 1000000 for microseconds.
        accessTime = deltaT.total_seconds() * 1000

        yList.append(accessTime)

    file.write('  <Axes>\n')
    file.write('    <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">String Size</XAxis>\n')
    file.write('    <YAxis min="'+str(min(yList))+'" max="'+str(max(yList))+'">Microseconds</YAxis>\n')
    file.write('  </Axes>\n')

    file.write('  <Sequence title="String Comparison" color="red">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yList[i])+'"/>\n')

    file.write('  </Sequence>\n')
    
    file.write('</Plot>\n')
    file.close()


if __name__ == "__main__":
    main()