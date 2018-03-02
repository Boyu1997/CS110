class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val


def make_list(root, lst):
    if root is None:
        return
    make_list(root.l_child, lst)
    lst.append(root.data)
    make_list(root.r_child, lst)


def maximum(root):
    if root.r_child is None:
        return root
    else:
        return maximum(root.r_child)


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
                root.l_child.parent = root
            else:
                insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
                root.r_child.parent = root
            else:
                insert(root.r_child, node)
    return root


def search(root, value):
    if root.data == value:
        return root
    elif root.data > value:
        if root.l_child is None:
            return None
        else:
            return search(root.l_child, value)
    else:
        if root.r_child is None:
            return None
        else:
            return search(root.r_child, value)


def transplant(root, u, v=None):
    if root == u:
        root = v
    else:
        if u.parent.l_child == u:
            u.parent.l_child = v
        else:
            u.parent.r_child = v
        if v is not None:
            v.parent = u.parent
    return root


def delete(root, node):

    # node has no children, remove node
    if node.l_child is None and node.r_child is None:
        transplant(root, node)

    # node has one child, move that child up
    elif node.l_child is None:
        transplant(root, node, node.r_child)
    elif node.r_child is None:
        transplant(root, node, node.l_child)

    # node has two children, replace the node by its successor than remove successor
    else:
        successor = maximum(node.l_child)
        node.data = successor.data
        transplant(root, successor, successor.l_child)
    return root


import random
import time

### small test case

# make a BST using insert function
r = None
for i in range(10):
    r = insert(r, Node(int(100*random.random())))

# print numbers in the BST in sorted order
lst = []
make_list(r, lst)
print "Small test case BST:", lst

# search a number in the BST
node = None
while node is None:
    node = search(r, int(100*random.random()))
print node.data, "is found in BST"

# remove the found node from BST
r = delete(r, node)
lst = []
make_list(r, lst)
print "BST afer delete is:", lst


### time comparison
print "\n"

# list insert
start_time = time.time()
l = []
for i in range(100000):
    l.append(int(1000000*random.random()))
end_time = time.time()
print "Insert 100000 numbers to a list takes", end_time-start_time

# BST insert
start_time = time.time()
r = None
for i in range(100000):
    r = insert(r, Node(int(1000000*random.random())))
end_time = time.time()
print "Insert 100000 numbers to a BST takes", end_time-start_time

# list search
start_time = time.time()
for i in range(1000):
    num = int(1000000*random.random())
    for j in range(100000):
        if l[j] == num:
            break
end_time = time.time()
print "Search 1000 numbers in a list takes", end_time-start_time

# BST search
start_time = time.time()
for i in range(1000):
    num = int(1000000*random.random())
    search(r, num)
end_time = time.time()
print "Search 1000 numbers in a BST takes", end_time-start_time

# list delete
start_time = time.time()
for i in range(1000):
    l.pop()
end_time = time.time()
print "Delete 1000 numbers from a list takes", end_time-start_time

# BST delete
start_time = time.time()
for i in range(1000):
    r = delete(r, r)
end_time = time.time()
print "Delete 1000 root nodes from a BST takes", end_time-start_time