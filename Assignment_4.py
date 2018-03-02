class LCS():
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def lenLCS(self, i, j):
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

DNA = [
    "TTCTACGGGGGGAGACCTTTACGAATCACACCGGTCTTCTTTGTTCTAGCCGCTCTTTTTCATCAGTTGCAGCTAGTGCATAATTGCTCACAAACGTATC",
    "TCTACGGGGGGCGTCATTACGGAATCCACACAGGTCGTTATGTTCATCTGTCTCTTTTCACAGTTGCGGCTTGTGCATAATGCTCACGAACGTATC",
    "TCTACGGGGGGCGTCTATTACGTCGCCAACAGGTCGTATGTTCATTGTCATCATTTTCATAGTTGCGGCCTGTGCGTGCTTACGAACGTATTCC",
    "TCCTAACGGGTAGTGTCATACGGAATCGACACGAGGTCGTATCTTCAATTGTCTCTTCACAGTTGCGGCTGTCCATAAACGCGTCCCGAACGTTATG",
    "TATCAGTAGGGCATACTTGTACGACATTCCCCGGATAGCCACTTTTTTCCTACCCGTCTCTTTTTCTGACCCGTTCCAGCTGATAAGTCTGATGACTC",
    "TAATCTATAGCATACTTTACGAACTACCCCGGTCCACGTTTTTCCTCGTCTTCTTTCGCTCGATAGCCATGGTAACTTCTACAAAGTTC",
    "TATCATAGGGCATACTTTTACGAACTCCCCGGTGCACTTTTTTCCTACCGCTCTTTTTCGACTCGTTGCAGCCATGATAACTGCTACAAACTTC"
]

L = LCS(DNA[0],DNA[1])
#L = LCS("ABCD","BCDE")
print L.lenLCS(len(L.list_1), len(L.list_2))

print L.lenTable  # NA represent data unrelevent to calculate LCS

# By reviewing the table, the point where NA grow in hight is where the i, j th element in both table are the same,
# which indicate point of mutation in the DNA

# When we observe a continuous set of such character, it is a high possibility that these sets comes from the same original DNA,
# as they are not only common, but also continuous.

# Algorism can use such character of continuous to find common DNA.