class Bloom():

    def __init__(self, length):
        self.length = length
        self.array = [0 for _ in range(length)]

    def insertion(self, number):
        self.array[number % self.length] = 1
        self.array[number * 2 % self.length] = 1
        self.array[number * 3 % self.length] = 1

    def lookup(self, number):
        if self.array[number % self.length] == 1\
                and self.array[number * 2 % self.length] == 1\
                and self.array[number * 3 % self.length] == 1:
            return True
        else:
            return False


import random
from itertools import izip
import matplotlib.pyplot as plt

false_postive = []
for i in range(1000, 20000, 1000):
    B = Bloom(i)
    input = [random.randrange(0,10000) for _ in range(1000)]
    set = iter(input)
    d = dict(izip(set, set))
    for num in input:
        B.insertion(num)
    postive = 0
    true_postive = 0
    for _ in range(1000):
        look = random.randrange(0, 10000)
        for _ in range(1000):
            if B.lookup(look) == True:
                postive += 1
                if look in d:
                    true_postive += 1
    false_postive.append((1.0*postive-true_postive)/postive)

plt.plot(false_postive)
plt.ylabel('False Positive Rate')
plt.show()



