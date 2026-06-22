import sys
from collections import deque

input = sys.stdin.readline

MOD = 10**9 + 7

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

dp = [0] * (n + 1)
dp[1] = 1

while q:
    now = q.popleft()

    for nxt in graph[now]:
        dp[nxt] = (dp[nxt] + dp[now]) % MOD
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

print(dp[n])