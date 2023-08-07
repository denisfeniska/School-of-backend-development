N = int(input())
numbers = [int(input()) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(i+1, min(i+8, N)):
        if (numbers[i] + numbers[j]) % 8 != 0:
            count += 1
print(count)
