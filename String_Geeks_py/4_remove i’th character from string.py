
def remove(string,index):
    newStr=''
    for i in range(len(string)):
        if i != index:
            newStr += string[i]
    return newStr
            
print(remove('malaya',1))