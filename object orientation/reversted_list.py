class ReversedList(object):
    def __init__(self, L):
        self.L = L[::-1]

    def __str__(self):
        return self.L

    def __len__(self):
        return len(self.L)

    def __getitem__(self, i):
        return self.L[i]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
