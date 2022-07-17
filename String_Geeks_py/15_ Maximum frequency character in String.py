
from collections import Counter


def maxfreq(str):
    
    myDist = Counter(str)
    maximum = max(myDist.values())
    
    for i in myDist.keys():        
        if myDist[i] == (maximum):
            print(i+" is maximum")
            
maxfreq('malmaya')