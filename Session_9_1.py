import random
import numpy as np
import matplotlib.pyplot as plt

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


def depth_of_cmp(bst, depth, lst):
    if bst.l_child is not None:
        lst = depth_of_cmp(bst.l_child, depth+1, lst)
    if bst.r_child is not None:
        lst = depth_of_cmp(bst.r_child, depth + 1, lst)
    lst.append(depth)
    return lst


def avg_cmp(bst):
    lst = []
    depth_of_cmp(bst, 0, lst)
    return np.mean(lst)


def max_height(bst, depth=0, max_depth=0):
    if bst.l_child is not None:
        max_depth = max_height(bst.l_child, depth+1, max_depth)
    if bst.r_child is not None:
        max_depth = max_height(bst.r_child, depth+1, max_depth)
    max_depth = max(depth, max_depth)
    return max_depth


# small test case
r = None
for i in range(100):
    r = insert(r, Node(int(100000*random.random())))
print avg_cmp(r)
print max_height(r)


# plot
lst_avg_cmp = []
lst_max_height = []
for i in range(500, 1001, 500):
    lst_ith_avg_cmp = []
    lst_ith_max_height = []
    for j in range(50):
        r = None
        for i in range(i):
            r = insert(r, Node(int(100000*random.random())))
        lst_ith_avg_cmp.append(avg_cmp(r))
        lst_ith_max_height.append(max_height(r))
    lst_avg_cmp.append(np.mean(lst_ith_avg_cmp))
    lst_max_height.append(np.mean(lst_ith_max_height))

plt.subplot(223)
plt.plot([x for x in range(500, 1001, 500)], lst_avg_cmp, label="average depth")
plt.plot([x for x in range(500, 1001, 500)], lst_max_height, label="maximum depth")
plt.xlabel("length")
plt.ylabel("depth")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.show()



class NodeCont:
    def __init__(self, val):
        self.l_child = None
        self.l_count = 0
        self.r_child = None
        self.parent = None
        self.data = val

def insert_count(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            root.l_count += 1
            if root.l_child is None:
                root.l_child = node
                root.l_child.parent = root
            else:
                insert_count(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
                root.r_child.parent = root
            else:
                insert_count(root.r_child, node)
    return root

def SELECT(bst, k):
    print bst.data, bst.l_count, k
    if bst.l_count > k:
        print "left"
        return SELECT(bst.l_child, k)
    elif bst.l_count < k:
        print "right"
        return SELECT(bst.r_child, k - bst.l_count - 1)
    else:
        return bst.data


def Rank(bst, value, k=0):
    if bst.data == value:
        k += bst.l_count
    elif bst.data > value:
        if bst.l_child is None:
            return None
        else:
            k = Rank(bst.l_child, value, k)
    else:
        if bst.r_child is None:
            return None
        else:
            k = k + bst.l_count + 1
            k = Rank(bst.r_child, value, k)
    return k


r = None
for i in range(100):
    r = insert_count(r, NodeCont(int(100000*random.random())))


selected = SELECT(r, 10)
print selected
lst = []
make_list(r, lst)
lst= sorted(lst)
print lst

print Rank(r, selected)



