# selection shot algorithm
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index]>list[j]:
                min_index= j

        list[i],list[min_index]=list[min_index], list[i]
    return list

# quickshot algorithm
def quick_short(list):
    length_of_list = len(list)
    if length_of_list <= 1:
        return list
    else:
        pivot = list.pop()
        
    pivot_grearer =[]
    pivot_smaller =[]
    for i in list:
        if i > pivot:
            pivot_grearer.append(i)
        else:
            pivot_smaller.append(i)
    return quick_short(pivot_smaller) + [pivot] + quick_short(pivot_grearer)

# Bubble sort algorithm
def bubble_sort(list):
    iteration_length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(iteration_length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]

    return list

#####################################################################
# list = [3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]
print(selection_sort([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))
print(quick_short([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))
print(bubble_sort([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))