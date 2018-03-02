import random

def quick_sort(list, s, e):
    if e-s <= 1:
        return
    pivot = s
    for_small = True
    for i in range(s+1,e):
        print i, pivot, list[i], list[pivot], for_small
        print list
        if for_small:
            if list[i] < list[pivot]:
                list[i], list[pivot] = list[pivot], list[i]
                pivot = i
                for_small = False
        else:
            if list[i] > list[pivot]:
                list[i], list[pivot] = list[pivot], list[i]
                pivot = i
                for_small = True
    print s, pivot, e
    quick_sort(list, s, pivot)
    quick_sort(list, pivot, e)

list = [random.randrange(100) for i in range(10)]
print list
quick_sort(list, 0, len(list))
print list