from sortedcontainers import SortedSet
N, M = map(int, input().split())
ss = SortedSet()

for _ in range(N):
    x, y = tuple(map(int, input().split()))
    ss.add((x, y))

for _ in range(M):
    x, y = tuple(map(int, input().split()))
    index = ss.bisect((x, y))
    if index == len(ss):
        print(-1, -1)
    else:
        print(*ss[index])

