import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def find_farthest(start):
    visited = [False] * (N + 1)
    stack = [(start, 0)]
    visited[start] = True

    farthest_node = start
    max_distance = 0

    while stack:
        node, distance = stack.pop()

        if distance > max_distance:
            max_distance = distance
            farthest_node = node

        for next_node, weight in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, distance + weight))

    return farthest_node, max_distance


a, _ = find_farthest(1)
b, diameter = find_farthest(a)

print(diameter)