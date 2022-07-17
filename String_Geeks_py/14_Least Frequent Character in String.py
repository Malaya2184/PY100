
from collections import Counter

def leastfeq(str):
    
    myDict=Counter(str)
    # instead of the above line ypu can write like this
    
    # ---------------------------------
    # myDict={}
    
    # for i in str:
    #     if i not in myDict.keys():
    #         myDict[i]=1
    #     else:
    #         myDict[i] +=1
    # ----------------------------------
    
    minim = min(myDict.values())
    
    for i in myDict.keys():
        if myDict[i] == minim:
            print(i + ' is minimum')
    

leastfeq('malaya')