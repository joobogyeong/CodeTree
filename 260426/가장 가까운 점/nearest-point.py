import heapq

N, M = map(int, input().split())
pq = []

for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(pq, (x+y, x, y))

for _ in range(M):
    new_x = pq[0][1] + 2
    new_y = pq[0][2] + 2
    heapq.heappop(pq)
    heapq.heappush(pq, (new_x+new_y, new_x, new_y))

print(pq[0][1], pq[0][2])