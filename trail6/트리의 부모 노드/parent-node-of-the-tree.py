import sys
sys.setrecursionlimit(100000)

N = int(input())
edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [0]*(N+1)

for _ in range(N-1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

def dfs(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            dfs(y)

visited[1] = True
dfs(1)

for i in range(2, N+1):
    print(parent[i])