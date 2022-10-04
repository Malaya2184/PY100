from enum import unique


arr = [12,1,2,3,4,5,6,7,8,9,8,5,4,3,21]
myDic = {}
noRepeat = []
unique = []

for i in arr:
    if i not in myDic.keys():
        myDic[i] = 0
    else:
        myDic[i] +=1
for i in myDic.keys():
    unique.append(i)
    if myDic[i] == 0:
        noRepeat.append(i)
        
print('no repeat numbers :-',noRepeat, 'unique numbers :-', unique)

