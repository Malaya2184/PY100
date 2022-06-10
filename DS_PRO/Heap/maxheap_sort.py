arr = [3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]
# max-heap sort will lead the array to assending order
def maxheap(arr,p):
    
    for i in range(len(arr)-p):
        if i > 0:
            child = i
            parent = (i+1)//2 - 1
            
            while arr[child]> arr[parent] and child !=0:
                arr[child], arr[parent] = arr[parent], arr[child]
                child = parent
                parent = (parent+1)//2 -1
                
    
def heapsort(arr):
    for i in range(len(arr)):
        maxheap(arr,i)
        arr[0], arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[0]
        
    return arr
        

print(heapsort(arr))