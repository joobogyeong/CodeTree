import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)


need = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, k = map(int, input().split())


    graph[y].append((x, k))
    indegree[x] += 1

q = deque()


for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        need[i][i] = 1

while q:
    now = q.popleft()

    for nxt, cnt in graph[now]:

        for base in range(1, N + 1):
            need[nxt][base] += need[now][base] * cnt

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, N + 1):
    if need[N][i] > 0:
        print(i, need[N][i])