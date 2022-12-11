n = int(input())
d = {}
while n != 0:
    s = input()
    L = s.split(' : ')
    class1 = L[0]
    class2 = L[-1].split(' ')
    d.setdefault(class1, [])
    d[class1].append(class2)
    n -= 1
# print(d)

