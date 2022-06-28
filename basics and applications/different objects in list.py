objects = [1, 2, 1, 2, 3]
ans = 0
L = []
for obj in objects: # доступная переменная objects
    if obj not in L:
        L.append(obj)
print(len(L))
