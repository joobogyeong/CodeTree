import heapq

N = int(input())
pq = []

for _ in range(N):
    cmd = input().split()
    if cmd[0]=='push':
        heapq.heappush(pq, -int(cmd[1]))
    elif cmd[0]=='pop':
        print(-pq[0])
        heapq.heappop(pq)
    elif cmd[0]=='size':
        print(len(pq))
    elif cmd[0]=='empty':
        if len(pq)==0:
            print(1)
        else:
            print(0)
    else:
        print(-int(pq[0]))

