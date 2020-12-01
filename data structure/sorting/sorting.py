# selection shot algorithm

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index]>list[j]:
                min_index= j

        list[i],list[min_index]=list[min_index], list[i]
    return list


# TODO: It is not an efficent program for the solution
# quickshot algorithm
def quick_short(list):
    length_of_list = len(list)
    if length_of_list <= 1:
        return list
    else:
    # here the pop method automatically poped out the last element of the list and return the list to the functiom
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


# insertion shot algorithm
def insertion_sort(list):
    for i in range(1, len(list)):
        while list[i-1] > list[i] and i>0:
            list[i-1],list[i] = list[i], list[i-1]
            i = i-1
    
    return list

# Merge sort algoruthm
    # merge sort for two sorted array

def merge_two_sorted_list(list1, list2):
    sorted_list= []
    i =0
    j =0
    while i< len(list1) and j< len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1

        else:
            sorted_list.append(list2[j])
            j += 1

    #these two loops added for the iteration when one of the list iteration terminated


    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1
    return sorted_list


    # merge sort algo (which will be a recurssive function )
def merge_two_unsorted_list(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    left = merge_two_unsorted_list(left)
    right = merge_two_unsorted_list(right)

    return merge_two_sorted_list(left,right)

# ####################################################################
# *********heap sort algorithm using min-hip***********
# def max_heap(list, p_node):

#     while p_node >= 0:
#         left_node = 2*p_node + 1
#         right_node = 2*p_node + 2
#         if list[left_node] > list[right_node] and list[left_node] > list[p_node]:
#             list[p_node], list[left_node] = list[left_node], list[p_node]
#             # p_node = p_node-1

#         elif list[right_node] > list[left_node] and list[right_node] > list[p_node]:
#             list[p_node], list[right_node] = list[right_node], list[p_node]
#             # p_node = p_node-1

# # heap sort algo
# def heap_sort(list,p_node):
#     length_of_list = int(len(list))-1
#     for i in range(p_node,-1,-1):
#         max_heap(list,p_node)
#     for i in range(length_of_list,-1,-1):
#         list[length_of_list], list[0] = list[0], list[length_of_list]
#     return list
            


# list = [33,35,42,10,7,8,14,19,48]
# p_node = int(len(list)//2)-1
# print(heap_sort(list,p_node))

#####################################################################
# list = [3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]
print(selection_sort([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))
print(quick_short([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))
print(bubble_sort([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))
print(insertion_sort([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))
print(merge_two_sorted_list([3, 4, 5, 5, 7, 8, 31, 67],[0, 1, 2, 2, 3, 90, 567]))
print(merge_two_unsorted_list([3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]))