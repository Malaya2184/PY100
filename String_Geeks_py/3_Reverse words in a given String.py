
def reverseWord(str):
    myArr=str.split(' ')
    myArr.reverse()
    return " ".join(myArr)


print(reverseWord('malaaya kumar'))