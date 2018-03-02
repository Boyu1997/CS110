# assuming mx is the startig and ending point of the max sub array in x[0:-2]
def incremental_max_subarray(x, mx):
    sum = 0
    for i in range(mx[1],len(x)):
        sum += x[i]
    if sum >=0:
        mx[1] = len(x)
    return mx

print incremental_max_subarray([-2,1,-3,4,-1,2,1,-5,4,0], [4,7])