myarray = [0,1,1,0,0,1,0]
j = 1

def sort(array):
    for i in range (0,len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j] :
                array[i] , array[j] = array[j] , array[i]
            else:
                j += 1
                
    return array
    
                
print(sort(myarray))