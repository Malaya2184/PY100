


arr = [3,7,10,12]
newArr=[]
i=0
status = True
while i < len(arr):
    if status is False:
        i-=1
    if i+1<len(arr) and arr[i]+1 != arr[i+1]:
        newArr.append(arr[i]+1)
        arr[i] = arr[i]+1
        i+=1
        status = False
    else:
        i+=1
        status=True

print(newArr)

    