import random

# O(n^2) easy to understand selection sort
def selection_sort(list):
    for i in range(len(list)):
        this_min = i
        for j in range(i, len(list)):
            if list[j] < list[this_min]:
                this_min = j
        list[i], list[this_min] = list[this_min], list[i]
    return list



def ms_merge(list_1, list_2):
    list = []
    pointer_1 = 0
    pointer_2 = 0
    for i in range(len(list_1) + len(list_2)):
        if pointer_1 == len(list_1):
            list.append(list_2[pointer_2])
            pointer_2 += 1
        elif pointer_2 == len(list_2):
            list.append(list_1[pointer_1])
        else:
            if list_1[pointer_1] < list_2[pointer_2]:
                list.append(list_1[pointer_1])
                pointer_1 += 1
            else:
                list.append(list_2[pointer_2])
                pointer_2 += 1

def midium(num_1, num_2, num_3):
    for i in range(7):
        if num_1 <= num_2 <= num_3:
            return num_2
        if i % 2 == 0:
            num_1, num_2 = num_2, num_1
        if i % 2 == 1:
            num_2, num_3 = num_3, num_2

def quick_sort(list):
    stack = [(0,len(list)-1)]
    while stack:
        start, end = stack.pop()
        pivit = midium(list[start], list[end/2], list[end])
        smaller = 0
        equal = 0
        bigger = 0
        while(smaller+equal+bigger < end-start+1):
            if list[start+smaller+equal] > pivit:
                list[start+smaller+equal], list[end-bigger] = list[end-bigger], list[start+smaller+equal]
                bigger += 1
            elif list[start+smaller+equal] < pivit:
                list[start+smaller+equal], list[start+smaller] = list[start+smaller], list[start+smaller+equal]
                smaller += 1
            else:
                equal += 1
        # print list, start, end, pivit, smaller, equal, bigger
        if smaller != 0: stack.append((start, start+smaller-1))
        if bigger != 0: stack.append((end-bigger+1, end))
    return list

def check_sorted(list):
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True




test_list = [int(100*random.random()) for _ in range(1000)]
print check_sorted(quick_sort(test_list))


