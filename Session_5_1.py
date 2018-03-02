import random

def is_sorted(list):
    last_num = list[0]
    for i in range(1, len(list)):
        if last_num > list[i]:
            return False
        last_num = list[i]
    return True

def shuffle(list):
    new_list = []
    while len(list):
        new_list.append(random.choice(list))
        list.remove(new_list[-1])
    return new_list

def random_sort(list):
    attemp_counter = 0
    while not is_sorted(list):
        list = shuffle(list)
        attemp_counter += 1
    return attemp_counter


test_case = [1, 5, 5, 2, 9]
print random_sort(test_case), "attempts to sort the test case"



def check_midium(num, list, delta):
    smaller = 0
    for i in range():
        if list[i] < num:
            smaller += 1
    if (smaller * 1.0) / len(list) > 0.5 - delta / 0.02 and (smaller * 1.0) / len(list) < 0.5 + delta / 0.02:
        return True
    else:
        return False


def random_midium(list, delta):
    is_midium = False
    attemp_counter = 0
    while not is_midium:
        num = random.choice(list)
        is_midium = check_midium(num, list, delta)
        attemp_counter += 1
    return attemp_counter

print random_midium(test_case, 0.4)
