def max_profit(lst):
    lst_len = len(lst)

    if len(lst) % 2 is 0:
        cut_len = 2
        lst_len -= 1
    else:
        cut_len = 1

    profit_lst = []
    for i in range(lst_len):
        if cut_len is 1:
            profit_lst.append(lst[i])
        elif cut_len is 2:
            profit_lst.append(max(lst[i], lst[i + 1]))

    print profit_lst

def max_profit_rec(lst, my=False, lib=[]):
    if my is False:
        my = True
    else:
        my = False
    if len(lst) is 2:
        if my:
            return max(lst[0], lst[1])
        else:
            return min(lst[0], lst[1])
    else:
        if my:
            p1 = max_profit_rec(lst[0:-1], my) + lst[-1]
            p2 = max_profit_rec(lst[1:], my) + lst[0]
            return max(p1, p2)
        else:
            p1 = max_profit_rec(lst[0:-1], my)
            p2 = max_profit_rec(lst[1:], my)
            return max(p1, p2)



max_profit([2, 10, 1, 5])

print max_profit_rec([2, 10, 1, 5])