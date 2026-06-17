import sys

N = int(input())
arr = list(map(int, input().split()))
max_sum = -sys.maxsize
sum = 0

for elem in arr:
    sum+=elem
    if sum < 0:
        max_sum = max(max_sum, sum)
        sum = 0
    else:
        max_sum = max(max_sum, sum)
print(max_sum)
