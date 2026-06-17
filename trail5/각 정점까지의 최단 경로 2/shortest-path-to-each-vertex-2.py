import sys

input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e18)

dist = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 거리는 0
for i in range(1, N + 1):
    dist[i][i] = 0

# 방향 그래프 간선 입력
for _ in range(M):
    a, b, weight = map(int, input().split())

    # 같은 방향 간선이 여러 개 들어올 수 있다면 더 짧은 것만 저장
    dist[a][b] = min(dist[a][b], weight)

# 플로이드-워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == INF:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()