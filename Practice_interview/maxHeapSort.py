from re import I

from Practice_interview.maxheap_sort import maxheap


arr = [3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]


def heapify(arr,p):
    
    for i in range(len(arr)-p):
        
        if i > 0:
            child = i
            parent = (i+1)//2-1
            
            while arr[child]> arr[parent]:
                
                arr[child], arr[parent] = arr[parent], arr[child]
                
                child = parent
                parent = (child+1)//2 -1
                
def heapsort(arr):
    
    for i in range(len(arr)):
        maxheap(arr,i)
        
        arr[0], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[0]
        
    return arr
            