
from collections import Counter


def findOddFreq(str):
    
    
    myDist = Counter(str)
    
    for i in myDist:
        if myDist[i] % 2 == 1:
            print(i + ' has odd frequensy')
            
            
findOddFreq('malaya kumar swain')