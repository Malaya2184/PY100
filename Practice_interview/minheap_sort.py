arr = [3,4,5,1,2,3,7,8,90,67,31,2,5,567]

# inheap_sort will lead the array to descending order 
def minheap(arr,p):
    for i in range(len(arr)-p):
        if i > 0:
            child = i
            parent = (i+1)//2 -1
            while arr[parent]>arr[child] and child !=0:
                arr[parent],arr[child]=arr[child],arr[parent]
                child = parent
                parent = (parent+1)//2 -1
                

def heapsort(arr):
    for i in range(len(arr)):
        minheap(arr,i)
        arr[0], arr[len(arr)-i-1]=arr[len(arr)-i-1], arr[0]
    return arr

print(heapsort(arr))