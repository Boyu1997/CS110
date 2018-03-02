import random

def qselect(lst, k):
    pivit = [lst.pop()]
    max = []
    min = []
    for num in lst:
        if num > pivit[0]:
            max.append(num)
        elif num == pivit[0]:
            pivit.append(num)
        else:
            min.append(num)
    print min, max, pivit
    if len(min) < k <= len(min)+len(pivit):
        return pivit[0]
    elif len(min) >= k:
        return qselect(min, k)
    else:
        return qselect(max, k-len(min)-len(pivit))



print qselect([5,2,8,7,1,3,9,4,6], 5)

test_list = [int(100*random.random()) for _ in range(1000)]
k = 36
print qselect(test_list, k) == sorted(test_list)[k-1]



import heapq

def median(minh, maxh):
    maxh_max = -1 * minh[0]
    minh_min = maxh[0]
    if (len(minh)+len(maxh)) % 2 == 0:
        return (maxh_max + minh_min) / 2
    else:
        return maxh_max

def add_to_median_heap(minh, maxh, a):
    if len(minh) == 0: heapq.heappush(minh, -1*a)
    else:
        maxh_max = -1 * minh[0]
        if a > maxh_max:
            heapq.heappush(maxh, a)
        else:
            heapq.heappush(minh, -1*a)
        if len(minh) > len(maxh) + 1:
            heapq.heappush(maxh, -1*heapq.heappop(minh))
        elif len(minh) < len(maxh):
            heapq.heappush(minh, -1*heapq.heappop(maxh))

minh = []
maxh = []
heapq.heapify(minh)
heapq.heapify(maxh)
for a in range(1, 100, 2):
    add_to_median_heap(minh, maxh, a)
print(median(minh, maxh))


def min_heap_add(lst, a):
    index = len(lst)
    lst.append(a)
    while(index != 0):
        if lst[index] > lst[index/2]:
            lst[index], lst[index/2] = lst[index/2], lst