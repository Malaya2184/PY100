
def capitalizeWord(str):
    
    myArr = str.split(' ')
    for i in range (len(myArr)):
        myArr[i]= myArr[i][0].upper() + myArr[i][1:len(myArr[i])-1] + myArr[i][len(myArr[i])-1].upper()
    return ' '.join(myArr)

print(capitalizeWord('malaya kumar'))