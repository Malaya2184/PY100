
from pandas import pivot


arr = [15,17,1,2,3,99,86,75,89]

#  selection sort

def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]> arr[j]:
                arr[i], arr[j] = arr[j],arr[i]
    return arr

# bubble sort
def bubbleSort(arr):
    
    sorted = False
    i =0
    while not sorted:
        sorted = True
        for j in range(len(arr)-1-i):
            if arr[j+1]< arr [j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                sorted = False
                
        i+=1
        
    
    return arr
   
 # quick sort  
def quickSort(arr):
    if len(arr)>1:
        pivot = arr.pop()
        pivot_smaller = []
        pivot_greater = []
        
        for i in arr:
            if i > pivot:
                pivot_greater.append(i)
            else:
                pivot_smaller.append(i)
                
        return quickSort(pivot_smaller)+[pivot]+ quickSort(pivot_greater)
         
    else:
        return arr       


            
            
            

print(selectionSort([15,17,1,2,3,99,86,75,89]))
print(bubbleSort([15,17,1,2,3,99,86,75,89]))
print(quickSort([15,17,1,2,3,99,86,75,89]))