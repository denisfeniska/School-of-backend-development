import numpy as np


class Table:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.zeros_array = np.zeros((rows, cols), 'int')
        self.new_row = np.zeros(cols, 'int')
        self.new_col = np.zeros(rows, 'int')

    def get_value(self, row, col):
        if row >= self.rows or col >= self.cols:
            return None
        else:
            return self.zeros_array[row][col]

    def set_value(self, row, col, value):
        self.zeros_array[row][col] = value
        return self.zeros_array

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        self.zeros_array = np.delete(self.zeros_array, row, axis=0)
        return self.zeros_array

    def delete_col(self, col):
        self.zeros_array = np.delete(self.zeros_array, col, axis=1)
        return self.zeros_array

    def add_row(self, row):
        self.zeros_array = np.insert(
            self.zeros_array, row, self.new_row, axis=0)
        return self.zeros_array

    def add_col(self, col):
        self.zeros_array = np.insert(
            self.zeros_array, col, self.new_col, axis=1)
        return self.zeros_array


tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
tab.add_row(1)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()