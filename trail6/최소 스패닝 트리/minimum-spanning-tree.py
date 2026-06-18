import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra
        return True
    return False

answer = 0

for w, a, b in edges:
    if union(a, b):
        answer += w

print(answer)