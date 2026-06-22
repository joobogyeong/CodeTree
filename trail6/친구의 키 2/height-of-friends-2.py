from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

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
    print("Consistent")
else:
    print("Inconsistent")