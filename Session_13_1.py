import hashlib


def which_problem(email, seminar, problems):
    email = email.strip().lower()
    assert "@minerva.kgi.edu" in email
    seminar = seminar.strip().lower()
    md5 = hashlib.md5(email + seminar).hexdigest()
    ind = int(md5, 16) % len(problems)
    return problems[ind]


email = 'boyu.jiang@minerva.kgi.edu'
print(which_problem(email, '12.1', ['directions', 'aquarium', 'baggage']))


# Directions:
# -----------
#
# You and your friends rented a bus and have gotten lost.  This is because the
# person with the map was sitting at the back of the bus and gave directions to
# the person in front of them.  This person then told the person in front of them.
# Eventually the directions reached the driver in the front.  Occasionally someone
# would make a mistake, and they would either:
#  - leave out a step,
#  - add a step,
#  - give the wrong instruction.
#
# Each direction was either "Straight", "Left", or "Right".
#
# You and you friends would like to figure out who made the most mistakes.
# Fortunately everyone wrote down the instructions they gave. Write a function
# ('blame') to figure out who is to blame.
#


class LCS():
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
        self.len_1 = len(list_1)
        self.len_2 = len(list_2)

    def lenLCS(self):
        i = self.len_1
        j = self.len_2
        self.lenTable = [["NA" for _ in range(j)] for _ in range(i)]
        self.lenCS(i, j)
        return self.lenTable[i-1][j-1]

    def lenCS(self, i, j):
        if self.lenTable[i-1][j-1] != "NA":
            return self.lenTable[i-1][j-1]
        if i == 0:
            for a in range(j):
                if self.list_1[0] == self.list_2[a]:
                    self.lenTable[i-1][j-1] = 1
                    return self.lenTable[i-1][j-1]
            return 0

        if j == 0:
            for a in range(i):
                if self.list_2[0] == self.list_1[a]:
                    self.lenTable[i-1][j-1] = 1
                    return self.lenTable[i-1][j-1]
            return 0

        if self.list_1[i-1] == self.list_2[j-1]:
            self.lenTable[i-1][j-1] = self.lenCS(i-1, j-1) + 1
            return self.lenTable[i-1][j-1]
        else:
            self.lenTable[i-1][j-1] = max(self.lenCS(i - 1, j), self.lenCS(i, j - 1))
            return self.lenTable[i-1][j-1]

def blame(directions):
    last_direction = directions.pop(0)
    for direction in directions:
        l = LCS(last_direction[1], direction[1])
        error = len(direction[1]) - l.lenLCS()
        print last_direction[1]
        print direction[1]
        print l.lenLCS()
        print direction[0], error
        last_direction = direction

directions = [('map', 'SSSRSSLRLS'), ('jane', 'SSRSLSLSSRLS'), ('jayna',
               'SRSLSLSRLS'), ('jomo', 'SRSLRRSLSRSLSR')]

print(blame(directions))


#Pepe
directions = [('map', 'SSSRSSLRLS'), ('jane', 'SSRSLSLSSRLS'), ('jayna',
                'SRSLSLSRLS'), ('jomo', 'SRSLRRSLSRSLSR')]

def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return C[m-1][n-1]


def blame(directions):
    mistakes = []
    original = directions.pop(0)
    orig_len = len(original[1])
    for person in directions:
        length = len(person[1])
        no_of_mis = len(original[1]) - LCS(original[1],person[1])
        if len(original[1]) < len(person[1]):
            no_of_mis += len(person[1])-len(original[1])
        original = person
        mistakes.append(no_of_mis)
    blamed_index = mistakes.index(max(mistakes))
    print mistakes
    return directions[blamed_index][0]

print(blame(directions))