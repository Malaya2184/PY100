
def upperHaf(str):
    
    mid = len(str)//2
    
    newStr = str[:mid]+str[mid:].upper()
    return newStr

print(upperHaf('malaya'))