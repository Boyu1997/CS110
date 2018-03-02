import random
import string
import numpy as np


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def empty_hash_table(N):
    return [[] for _ in xrange(N)]


def add_to_hash_table(hash_table, item, hash_function):
    N = len(hash_table)
    # Your code here
    hash_id = hash_function(item)
    hash_id = hash_id % N

    # Another way to fit into hash table
    # while hash_id >= N:
    #     hash_id -= N

    hash_table[hash_id].append(item)
    return hash_table


def contains(hash_table, item, hash_function):
    N = len(hash_table)
    # Your code here
    hash_id = hash_function(item)
    while hash_id >= N:
        hash_id -= N
    for key, element in enumerate(hash_table[hash_id]):
        if element == item:
            return True
    return False
    # return true if the item has already been stored in the hash_table


def remove(hash_table, item, hash_function):
    if not contains(hash_table, item, hash_function):
        raise ValueError()
    # Your code here
    N = len(hash_table)
    hash_id = hash_function(item)
    while hash_id >= N:
        hash_id -= N
    hash_table[hash_id].remove(item)
    return hash_table


def hash_str1(string):
    ans = 0
    for chr in string:
        ans += ord(chr)
    return ans


def hash_str2(string):
    ans = 0
    for chr in string:
        ans = ans ^ ord(chr)
    return ans


def hash_str3(string):
    ans = 0
    for chr in string:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(string):
    random.seed(ord(string[0]))
    return random.getrandbits(32)

word_set = [''.join([random.choice(string.ascii_letters) for _ in xrange(10)]) for _ in xrange(1000000)]


hash_function_list = [hash_str1, hash_str2, hash_str3, hash_str4]
for hash_function in hash_function_list:
    hash_table = empty_hash_table(5000)
    for word in word_set:
        add_to_hash_table(hash_table, word, hash_function)
    length = []
    for set in hash_table:
        length.append(len(set))
    print "Hash:", hash_function, "Mean:", np.mean(length), "Max:", np.max(length), "Midium", np.median(length)
    print "99.9%:", np.percentile(length, 99.9), "99%:", np.percentile(length, 99), "90%:", np.percentile(length, 90)