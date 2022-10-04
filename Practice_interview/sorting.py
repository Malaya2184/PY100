
myarr = [11,22,32,2,34,98,56]
#  selectrion sort
def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# bubble sort
def bubbleSort(arr):
    sorted = False
    
    while not sorted:
        sorted = True
        i=0
        for i in range(len(arr)-1-i):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

                sorted = False
    return arr

def insertionSort(arr):

    for i in range(1,len(arr)):
        while arr[i]<arr[i-1] and i !=0:
            arr[i],arr[i-1]= arr[i-1], arr[i]
            i-=1
    return arr

def quickSort(arr):
    if len(arr) > 1:
        pivot = arr.pop()
        pivot_smaller=[]
        pivot_greater = []
        for i in arr:
            if i > pivot:
                pivot_greater.append(i)
            else:
                pivot_smaller.append(i)
                
        return quickSort(pivot_smaller) +[pivot] + quickSort(pivot_greater)
    else:
        return arr
        
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right= arr[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
    else:
        return arr
    
    i=0
    j=0
    sorted=[]
    while i + j != len(left)+len(right):
        if i == len(left):
            sorted.extend(right[j:])
            j = len(right)
        elif j == len(right):
            sorted.extend(left[i:])
            i=len(left)
        elif left[i]< right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    return sorted
    
    
    
print("selection sort---->", selectionSort([11,22,32,2,34,98,56]))
print("bubble sort---->", bubbleSort([11,22,32,2,34,98,56]))
print("bubble sort---->", bubbleSort([11,22,32,2,34,98,56]))
print("insertion sort---->", insertionSort([11,22,32,2,34,98,56]))
print("quick sort---->", quickSort([11,22,32,2,34,98,56]))
print("merge sort---->", mergeSort([11,22,32,2,34,98,56,100]))