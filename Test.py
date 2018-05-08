import sys


l = [["-" for _ in range(3)] for _ in range(3)]

def print_bord(l):
    for line in l:
        for key, ele in enumerate(line):
            if key is 2:
                print ele
            else:
                sys.stdout.write('%s|' % (ele))

def ask_input():
    (m, n) = input("Input line and colom to place:")
    return m, n

def place_x(l, m, n):
    while m > 3 or n > 3:
        print "Wrong input"
        m, n = ask_input()
    while l[m-1][n-1] is "x":
        print "Wrong input"
        m, n = ask_input()
    l[m-1][n-1] = "x"
    return l


print_bord(l)
total_count = 0
while total_count < 10:
    m, n = ask_input()
    l = place_x(l, m, n)
    total_count += 1
    print_bord(l)