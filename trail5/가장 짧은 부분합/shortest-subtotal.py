import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 0
sum_val = 0
answer = sys.maxsize
while i < N:
    while j < N and sum_val < S:
        sum_val += arr[j]
        j += 1

    if sum_val >= S:
        answer = min(answer, j - i)

    sum_val -= arr[i]
    i += 1
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)