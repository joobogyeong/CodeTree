import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, weight = map(int, input().split())

    graph[a].append((b, weight))

    reverse_graph[b].append((a, weight))


def dijkstra(start, graph):
    INF = int(1e18)
    dist = [INF] * (N + 1)

    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))  # (현재 거리, 현재 정점)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for next_node, weight in graph[current_node]:
            next_dist = current_dist + weight

            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

    return dist


# X에서 각 정점으로 가는 최단거리
from_x = dijkstra(X, graph)

# 각 정점에서 X로 가는 최단거리
# 방향을 뒤집은 그래프에서 X를 시작점으로 돌리면 됨
to_x = dijkstra(X, reverse_graph)

answer = 0

for i in range(1, N + 1):
    round_trip = to_x[i] + from_x[i]
    answer = max(answer, round_trip)

print(answer)