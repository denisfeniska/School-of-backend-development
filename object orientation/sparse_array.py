class SparseArray:
    def __init__(self) -> None:
        self.L = {}

    def __getitem__(self, i):
        return self.L.get(i, 0)

    def __setitem__(self, i, item):
        self.L[i] = item


arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))
