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

def max_profit_rec(lst, start, end, my=False, lib=dict()):
    if my is False:
        my = True
    else:
        my = False
    if end-start is 1:
        if my:
            return max(lst[start], lst[end])
        else:
            return min(lst[start], lst[end])
    elif start^end in lib.keys():
            return lib[start^end]
    else:
        if my:
            p1 = max_profit_rec(lst, start, end-1, my, lib) + lst[end]
            p2 = max_profit_rec(lst, start+1, end, my, lib) + lst[start]
            lib[start^end] = max(p1, p2)
            return lib[start^end]
        else:
            p1 = max_profit_rec(lst, start, end-1, my, lib)
            p2 = max_profit_rec(lst, start+1, end, my, lib)
            lib[start^end] = max(p1, p2)
            return lib[start^end]

lst = [2, 10, 1, 5]
print max_profit_rec(lst, 0, len(lst)-1)