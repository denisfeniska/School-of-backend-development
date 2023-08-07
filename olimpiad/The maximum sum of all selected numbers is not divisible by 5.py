N = int(input())
sum = 0
min_diff = float('inf')
for i in range(N):
    a, b = map(int, input().split())
    sum += max(a, b)
    if abs(a - b) % 5 != 0:
        min_diff = min(min_diff, abs(a - b))
if sum % 5 == 0:
    if min_diff == float('inf'):
        print(0)
    else:
        print(sum - min_diff)
else:
    print(sum)
