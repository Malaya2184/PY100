
def printEvenWords(str):
    
    myArr = str.split(' ')
    for i in myArr:
        if len(i)%2 == 0:
            print(i)
            
printEvenWords('Hii This is a python language')