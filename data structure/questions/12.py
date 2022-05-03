# sorting in array practice

#  selection sort

myarr = [11,22,32,2,34,98,56]

def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[i]):
                arr[i],arr[j]= arr[j],arr[i]
    return arr

# bubble sort algo in in one way
def bubbleSort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr

# bubble sort in anthor way i think while loop is better interms of best possible numbers of iteration for the bubble sort

def bubbleSortNew(arr):
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                sorted = False
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr
    
def quickSort(arr):
    if(len(arr)<=1):
        return arr
    else:
    
        pivot = arr.pop()
        pivot_greater=[]
        pivot_smaller=[]
        for i in arr:
            if(i > pivot):
                pivot_greater.append(i)
            else:
                pivot_smaller.append(i)
                
        return quickSort(pivot_smaller) + [pivot] + quickSort(pivot_greater)   
        
        
print("selection sort---> ",selectionSort([11,22,32,2,34,98,56]))
print("bubble sort---> ",bubbleSort([11,22,32,2,34,98,56]))
print("bubble new sort---> ",bubbleSortNew([11,22,32,2,34,98,56]))
print("quick sort---> ",quickSort([11,22,32,2,34,98,56]))
                
