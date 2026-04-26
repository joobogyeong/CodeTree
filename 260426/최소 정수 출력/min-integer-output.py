import heapq

N = int(input())
pq = []

for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if len(pq)==0:
            print(0)
        else:
            print(pq[0])
            heapq.heappop(pq)
    else:
        heapq.heappush(pq, cmd)