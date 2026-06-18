import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

for i in range(n):
    weights = list(map(int, input().split()))

    for j in range(m - 1):
        u = i * m + j
        v = i * m + (j + 1)

        edges.append((weights[j], u, v))

for i in range(n - 1):
    weights = list(map(int, input().split()))

    for j in range(m):
        u = i * m + j
        v = (i + 1) * m + j

        edges.append((weights[j], u, v))

edges.sort()

size = n * m
parent = list(range(size))

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

        if cnt == size - 1:
            break

print(answer)