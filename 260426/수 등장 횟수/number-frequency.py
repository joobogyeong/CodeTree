N, M = map(int, input().split())
arr = list(map(int, input().split()))
cmd = list(map(int, input().split()))
d = {}

for i in range(N):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]]+=1

for elem in cmd:
    if elem not in d:
        print(0, end=" ")
    else:
        print(d[elem], end=" ")