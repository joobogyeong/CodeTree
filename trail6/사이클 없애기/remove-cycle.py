import sys
from collections import deque

input = sys.stdin.readline

n, m1, m2 = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m1):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

undirected_edges = []
for _ in range(m2):
    a, b = map(int, input().split())
    undirected_edges.append((a, b))

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

count = 0

while q:
    cur = q.popleft()
    count += 1

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

if count == n:
    print("Yes")
else:
    print("No")