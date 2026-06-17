import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
graph = [[] for _ in range(N + 1)]

for idx in range(M):
    a, b, w = map(int, input().split())
    edges.append([a, b, w])
    graph[a].append((b, w, idx))
    graph[b].append((a, w, idx))


def dijkstra(save_path=False):
    INF = int(1e18)
    dist = [INF] * (N + 1)
    parent_edge = [-1] * (N + 1)

    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > dist[cur_node]:
            continue

        for next_node, weight, edge_idx in graph[cur_node]:
            a, b, original_weight = edges[edge_idx]
            weight = original_weight

            next_dist = cur_dist + weight

            if next_dist < dist[next_node]:
                dist[next_node] = next_dist

                if save_path:
                    parent_edge[next_node] = edge_idx

                heapq.heappush(pq, (next_dist, next_node))

    return dist[N], parent_edge


original_dist, parent_edge = dijkstra(True)

path_edges = []
cur = N

while cur != 1:
    edge_idx = parent_edge[cur]
    path_edges.append(edge_idx)

    a, b, w = edges[edge_idx]

    if cur == a:
        cur = b
    else:
        cur = a

max_dist = original_dist

for edge_idx in path_edges:
    edges[edge_idx][2] *= 2
    new_dist, _ = dijkstra(False)
    max_dist = max(max_dist, new_dist)
    edges[edge_idx][2] //= 2

print(max_dist - original_dist)