import numpy as np

class ILCELL():
    def __init__(self, key=None):
        self.key = key
        self.next = None

class NODE():
    def __init__(self, ckey=None, rank=None):
        self.ckey = ckey
        self.rank = rank
        self.next = None
        self.child = None
        self.il = ILCELL()
        self.il_tail = ILCELL()

class HEAD():
    def __init__(self, rank=None):
        self.rank = rank
        self.queue = NODE()
        self.next = None
        self.prev = None
        self.suffix_min = None


class SoftHeap():

    def __init__(self, r):
        self.header = HEAD()
        self.tail = HEAD(np.infty)
        self.header.next = self.tail
        self.tail.prev = self.header
        self.r = r

    def insert(self, newkey):
        l = ILCELL()
        l.key = newkey
        q = NODE(newkey, 0)
        q.il = l
        q.il_tail = l
        self.meld(q)

    def meld(self, q):
        h = HEAD()
        prevhead = HEAD()
        tohead = self.header.next
        top = NODE()
        bottom = NODE()
        while q.rank > tohead.rank:
            tohead = tohead.next
        prevhead = tohead.prev

        while q.rank == tohead.rank:
            if tohead.queue.ckey > q.ckey:
                top = q
                bottom = tohead.queue
            else:
                top = tohead.queue
                bottom = q
            q = NODE(top.ckey, top.rank+1)
            q.child = bottom
            q.next = top
            q.il = top.il
            q.il_tail = top.il_tail
            tohead = tohead.next

        if prevhead == tohead.prev:
            h = HEAD()
        else:
            h = prevhead.next
        h.queue = q
        h.rank = q.rank
        h.prev = prevhead
        h.next = tohead
        prevhead.next = h
        tohead.prev = h
        self.fix_minlist(h)

    def fix_minlist(self, h):
        tmpmin = HEAD()
        if h.next == self.tail:
            tmpmin = h
        else:
            tmpmin = h.next.suffix_min
        while h != self.header:
            if h.queue.ckey < tmpmin.queue.ckey:
                tmpmin = h
            h.suffix_min = tmpmin
            h = h.prev





SH = SoftHeap(0.3)
SH.insert(6)
SH.insert(7)
SH.insert(9)
SH.insert(3)

