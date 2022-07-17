

from collections import OrderedDict


def removeDuplicate(str):
    
    myDict = OrderedDict.fromkeys(str)
    
    return ''.join(myDict)

def removeDuplicate2(str):
    
    mySet = set(str)
    return ''.join(mySet)
    
print(removeDuplicate('malaya'))
print(removeDuplicate2('malaya'))