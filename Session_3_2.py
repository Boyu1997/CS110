import heapq
list = [39, 85, 85, 16, 49, 7, 49, 92, 76, 15, 21, 30, 29, 31, 28]
list = [list[i]*-1 for i in range(len(list))]
heapq.heapify(list)
list = [list[i]*-1 for i in range(len(list))]
print "max num", heapq.heappop(list)