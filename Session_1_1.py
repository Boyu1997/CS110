from random import randint;

def rand_list(m):
    lis = []
    for _ in xrange(m):
        lis.append(randint(-1000, 1000))
    return lis

def g(f, m, n):
    lis = []
    for i in range(n):
        lis.append([f[0:2*(i+1)]])
    return lis

a = 100
b = 5
c = 3
print g(rand_list(a), b, c)