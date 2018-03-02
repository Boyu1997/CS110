import numpy as np
import matplotlib.pyplot as plt
import random

old_ass = 0
total_ass = 0
ass_over_time = []
for _ in range(50000):
    new_ass = np.random.uniform(0,1,1)
    if new_ass > old_ass:
        total_ass += 1
        old_ass = new_ass
    ass_over_time.append(total_ass)

#plt.plot(ass_over_time)
#plt.xlabel('day')
#plt.ylabel('total ass')
#plt.show()



correct_lis = []
for i in range(1000):
    num_of_p = 10*i
    hats = random.sample([x for x in range(num_of_p)], num_of_p)
    correct = 0
    for j in range(num_of_p):
        the_hat = hats.pop()
        if the_hat == j:
            correct += 1
    correct_lis.append(correct)

plt.plot(correct_lis)
plt.show()