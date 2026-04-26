from sortedcontainers import SortedSet

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ss = SortedSet()
for elem in arr:
    ss.add(elem)

for _ in range(M):
    m = int(input())
    index = ss.bisect_left(m)
    if index < len(ss):
        print(ss[index])
    else:
        print('-1')