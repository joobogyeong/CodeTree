import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    parent[rb] = ra
    size[ra] += size[rb]

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'x':
        a = int(cmd[1])
        b = int(cmd[2])
        union(a, b)

    else:  # y a
        a = int(cmd[1])
        print(size[find(a)])