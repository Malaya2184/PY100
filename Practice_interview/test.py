
arr = [15,17,1,2,3,99,86,75,89]

def bubbleSort(arr):
     
    i = 0
    sorted = False
    
    while  not sorted:
        
        sorted = True
        
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
                
        i +=1
    
    return arr

print(bubbleSort(arr))