def insertion_sort(lis):
    step = 0
    for i in range(1, len(lis)):
        for j in range(0, i):
            if lis[j] > lis[i]:
                lis[i], lis[j] = lis[j], lis[i]
            step += 1
            print step, lis
        print "end"
    return lis

def bubble_sort(lis):
    step = 0
    for i in range(0, len(lis)):
        for j in range(1, len(lis)):
            if lis[j-1] > lis[j]:
                lis[j-1], lis[j] = lis[j], lis[j-1]
            step += 1
            print step, lis
        print "end"
    return lis


print "insertion sort", insertion_sort([1,5,3,4,7,2,5])
print "bubble sort", bubble_sort([1,5,3,4,7,2,5])