# sorting in array practice

#  selection sort

from ast import If


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
    
def insertationSort(arr):
    for i in range(len(arr)):
        while arr[i-1]>arr[i] and i!=0:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
            
    return arr
    
# sorting using one loop
# TODO: HAS NOT WORKED YET
def sortUsingOneloop(arr):
    i=0
    newloop=True
    
    while(i!=len(arr)-1):

        if(newloop):
            j=i+1
            newloop=False
        elif(j<len(arr) and arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        elif(j<len(arr) and arr[i]<arr[j]):
            j+=1
        else:
            i+=1
            newloop=True
            
    return arr

def sortOneloop(arr):
    i = 0
    newloop = True
    
    while(i<len(arr)-1):
        if(newloop):
            j=i+1
            newloop = False
        elif (j<len(arr) and arr[j]<arr[i]):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        elif(j == len(arr)):
            i+=1
            newloop=True
        else:
            j+=1
    return arr

def mergeSort(arr):
    if(len(arr)==1):
        return arr
    elif (len(arr)>1):
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left=mergeSort(left)
        right=mergeSort(right)
        
    i=0
    j=0
    sortedArr = []
    while i+j != len(left)+len(right):
        if i<len(left) and j<len(right) and left[i] < right[j]:
            sortedArr.append(left[i])
            i += 1

        elif i<len(left) and j<len(right) and left[i] > right[j]:
            sortedArr.append(right[j])
            j += 1
        elif(i==len(left)):
            sortedArr.extend(right[j:])
            j = len(right)
        elif(j==len(right)):
            sortedArr.extend(left[i:])
            i=len(left)
            
    return sortedArr
   
        
        

        
        
print("selection sort---> ",selectionSort([11,22,32,2,34,98,56]))
print("bubble sort---> ",bubbleSort([11,22,32,2,34,98,56]))
print("bubble new sort---> ",bubbleSortNew([11,22,32,2,34,98,56]))
print("quick sort---> ",quickSort([11,22,32,2,34,98,56]))
print("insertation sort---> ",insertationSort([11,22,32,2,34,98,56]))
print("sortUsingOneloop sort---> ",sortUsingOneloop([11,22,32,2,34,98,56]))
print("sortOneloop sort---> ",sortOneloop([11,22,32,2,34,98,56]))
print("mergeSort sort---> ",mergeSort([11,22,32,2,34,98,56,100]))
