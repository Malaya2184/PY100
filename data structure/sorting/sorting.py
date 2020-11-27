list = [3,4,5,1,2,3,0,7,8,90,67,31,2,5,567]
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index]>list[j]:
                min_index= j

        list[i],list[min_index]=list[min_index], list[i]
    return list

print(selection_sort(list))