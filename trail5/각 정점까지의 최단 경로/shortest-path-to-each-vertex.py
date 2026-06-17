import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, weight = map(int, input().split())

    # 무방향 그래프이므로 양쪽 모두 추가
    graph[a].append((b, weight))
    graph[b].append((a, weight))

INF = int(1e18)
dist = [INF] * (N + 1)

dist[K] = 0
pq = []
heapq.heappush(pq, (0, K))  # (거리, 정점)

while pq:
    current_dist, current_node = heapq.heappop(pq)

    # 이미 더 짧은 거리로 처리된 적 있으면 무시
    if current_dist > dist[current_node]:
        continue

    for next_node, weight in graph[current_node]:
        next_dist = current_dist + weight

        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))

for i in range(1, N + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])