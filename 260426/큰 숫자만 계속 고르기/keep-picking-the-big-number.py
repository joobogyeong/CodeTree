import heapq

N, M = map(int, input().split())
arr = list(map(int, input().split()))

pq = [-x for x in arr]
heapq.heapify(pq)

for _ in range(M):
    max_num = heapq.heappop(pq) + 1
    heapq.heappush(pq, max_num)

print(-heapq.heappop(pq))
    

