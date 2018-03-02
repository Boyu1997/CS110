import random

def merge_sort(list):
    if len(list) > 1:
        list_1 = merge_sort(list[:len(list)/2])
        list_2 = merge_sort(list[len(list)/2:])
        counter_1 = 0
        counter_2 = 0
        return_list = []
        for i in range(len(list)):
            if counter_1 >= len(list_1):
                return_list.append(list_2[counter_2])
                counter_2 += 1
            elif counter_2 >= len(list_2):
                return_list.append(list_1[counter_1])
                counter_1 += 1
            elif list_1[counter_1] < list_2[counter_2]:
                return_list.append(list_1[counter_1])
                counter_1 += 1
            else:
                return_list.append(list_2[counter_2])
                counter_2 += 1
        return return_list
    else:
        return list

print merge_sort([9,8,7,6,5,4,3,2,1])
print merge_sort([random.randrange(100) for i in range(100)])