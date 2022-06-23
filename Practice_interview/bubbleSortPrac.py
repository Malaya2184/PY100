myarr = [11,22,32,2,34,98,56]


def bubblesort(arr):
    
    sorted = False
    i =0
    while  not sorted:
        sorted = True
        
        for j in range(len(arr)-i-1):
            if arr[j+1]< arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                sorted = False
        i+=1
    return arr
        
print(bubblesort(myarr))