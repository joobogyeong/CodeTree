from sortedcontainers import SortedSet

N, M = map(int, input().split())
ss = SortedSet()

for i in range(1, M+1):
    ss.add(i)

arr = list(map(int, input().split()))
for n in arr:
    if n in ss:
        ss.remove(n)
        print(ss[-1])

