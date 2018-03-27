def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_with_cut(n, d={1:1,2:1}):
    if n in d:
        return d[n]
    else:
        d[n] = fib_with_cut(n-1, d) + fib_with_cut(n-2, d)
        return d[n]

def fib_bottom_upt(n):
    lst = [1,1]
    while len(lst) < n:
        lst.append(lst[-2]+lst[-1])
    return lst[-1]


import time

start_time = time.time()
print "fib 30 =", fib(30)
end_time = time.time()
print "Time to compute fib 30 is:", end_time-start_time

start_time = time.time()
print "fib 30 =", fib_with_cut(30)
end_time = time.time()
print "Time to compute fib 30 with cut is:", end_time-start_time

start_time = time.time()
print "fib 30 =", fib_bottom_upt(30)
end_time = time.time()
print "Time to compute fib 30 bottom up is:", end_time-start_time

print "==="
start_time = time.time()
print "fib 1000 =", fib_with_cut(1000)
end_time = time.time()
print "Time to compute fib 10000 with cut is:", end_time-start_time

start_time = time.time()
print "fib 1000 =", fib_bottom_upt(1000)
end_time = time.time()
print "Time to compute fib 10000 bottom up is:", end_time-start_time

