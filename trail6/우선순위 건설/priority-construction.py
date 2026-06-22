import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for pre in data[1:]:
        if pre == -1:
            break
        graph[pre].append(i)
        indegree[i] += 1

result = time[:]
q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if result[nxt] < result[cur] + time[nxt]:
            result[nxt] = result[cur] + time[nxt]
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print("\n".join(map(str, result[1:])))