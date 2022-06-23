str = ' malaya'

def invertStr(str):
    
    if len(str) == 1:
        return str
    
    else:
        return str[-1] + invertStr(str[:len(str)-1])
    
    
    
print(invertStr(str))           