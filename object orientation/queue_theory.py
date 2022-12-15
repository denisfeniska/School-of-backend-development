class Queue:
    def __init__(self, *values) -> None:
        self.L_values = list(values)

    def append(self, *values):
        self.L_values.extend(values)

    def copy(self):
        return Queue(*self.L_values)

    def pop(self):
        if len(self.L_values) == 0:
            return None
        else:
            first_el = self.L_values[0]
            self.L_values.pop(0)
            return first_el
    
    def extend(self, queue):
        self.L_values.extend(queue.L_values)
    
    def next(self):
        return Queue(*self.L_values[1:])

    def __add__(self, other):
        new_queue = self.copy()
        new_queue.L_values += other.L_values
        return new_queue

        # return Queue(*self.L_values, *other.L_values)

    def __iadd__(self, other):
        return Queue(*self.L_values, *other.L_values)

    def __eq__(self, other) -> bool:
        if len(self.L_values) != len(other.L_values):
            return False
        else:
            for i in range(len(self.L_values)):
                if self.L_values[i] != other.L_values[i]:
                    return False
            return True

    def __rshift__(self, N):
        # new_queue = self.copy()
        # if N > len(self.L_values):
        #     return []
        # else:
        #     new_queue = new_queue[N:]
        #     return new_queue

        
        L_values_new = self.L_values.copy()
        L_values_new = L_values_new[N:]
        new_queue = Queue(*L_values_new)
        return new_queue

    def __str__(self) -> str:
        if self.L_values:
            return "[" + " -> ".join(map(str, self.L_values)) + ']'
        else:
            return []

    def __next__(self):
        return self.next()

    
q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
