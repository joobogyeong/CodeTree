import sys
N = int(input())
line = [tuple(map(int, input().split())) for _ in range(N)]
max_sum = -sys.maxsize
checked = []
for x1, x2 in line:
    checked.append((x1, +1))
    checked.append((x2, -1))

checked.sort()
sum = 0
for x, v in checked:
    sum += v
    max_sum = max(sum, max_sum)

print(max_sum)