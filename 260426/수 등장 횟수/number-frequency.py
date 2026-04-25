N, M = map(int, input().split())
arr = list(map(int, input().split()))
d = {}

for _ in range(M):
    cmd = int(input())
    d[cmd] = 0

for i in range(M):
    for j in range(N):
        if arr[i]==d[j]:
            d[j]+=1

print(*d)