from collections import defaultdict, deque
from itertools import count

# Ref: https://cr.yp.to/bib/1975/aho.pdf
# Ref: https://www.hs-albsig.de/studium/\
# wirtschaftsinformatik/Documents/commentzwalterextab.pdf


class ACMachine:
    """Aho-Corasick Algorithm for String Matching"""

    def __init__(self):
        self.transitions = defaultdict(count(1).__next__)
        self.fails = defaultdict(lambda: 0)
        self.edges = defaultdict(set)
        self.output = defaultdict(set)

    def extend(self, wlist):
        list(map(lambda x: self.add(x), wlist))
        return self

    def add(self, word):
        """Add a word to the graph (Section 3 - Aho, Corasick 1975)"""
        """Construct the go to function"""
        state = 0
        for char in word:
            self.edges[state].add(char)
            state = self.transitions[state, char]

        self.output[state].add(word)
        return self

    def construct(self):

        """Construct the failure function (Section 3 - Aho, Corasick 1975)"""
        queue = deque()
        for char in self.edges[0]:
            status = self.transitions[0, char]
            queue.append(status)
        while queue:
            r = queue.popleft()
            if r in self.edges:
                for char in self.edges[r]:
                    if (r, char) in self.transitions:
                        s = self.transitions[r, char]
                        queue.append(s)
                        state = self.fails[r]
                        while state and (state, char) not in self.transitions:
                            state = self.fails[state]
                        if (state, char) in self.transitions:
                            self.fails[s] = self.transitions[state, char]
                        if s and state in self.fails and self.fails[state] in self.output:
                            self.output[s].update(self.output[self.fails[state]])
        return self

    def search(self, text):
        """Search in `text`"""
        state = 0

        for i, t in enumerate(text):
            while state and (state, t) not in self.transitions:
                state = self.fails[state]
            state = self.transitions[state, t]
            
            if self.output[state]:
                print('@', i, self.output[state])
        return self
