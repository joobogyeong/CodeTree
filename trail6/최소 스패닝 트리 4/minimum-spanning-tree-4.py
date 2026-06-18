import sys
input = sys.stdin.readline

n, m = map(int, input().split())

kind = [''] + input().split()

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())

    if kind[u] != kind[v]:
        edges.append((w, u, v))

edges.sort()

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return False

    parent[rb] = ra
    return True


answer = 0
cnt = 0

for w, u, v in edges:
    if union(u, v):
        answer += w
        cnt += 1

        if cnt == n - 1:
            break

if cnt == n - 1:
    print(answer)
else:
    print(-1)