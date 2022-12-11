x = int(input())
y = int(input())
z = int(input())
if x == y == z:
    print('equilateral')
elif x == y or x == z or y == z:
    print('isosceles')
else:
    print('versalite')
