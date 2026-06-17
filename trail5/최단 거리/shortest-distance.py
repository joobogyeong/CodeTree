import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dist = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for _ in range(M):
    a, b = map(int, input().split())
    print(dist[a - 1][b - 1])