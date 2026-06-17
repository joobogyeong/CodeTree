import heapq

n = int(input())

events = []

for i in range(n):
    y, x1, x2 = map(int, input().split())

    left = min(x1, x2)
    right = max(x1, x2)

    events.append((left, 1, y, i))    # 선분 시작
    events.append((right, -1, y, i))  # 선분 끝

events.sort()

active = [False] * n
heap = []
visible = set()

for idx in range(len(events)):
    x, event_type, y, line_id = events[idx]

    if event_type == 1:
        active[line_id] = True
        heapq.heappush(heap, (y, line_id))
    else:
        active[line_id] = False

    while heap and not active[heap[0][1]]:
        heapq.heappop(heap)

    if idx < len(events) - 1 and heap:
        visible.add(heap[0][1])

print(len(visible))