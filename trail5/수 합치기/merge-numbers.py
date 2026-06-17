import heapq

N = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
cost = 0

while len(arr)!=1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    c = a+b
    cost+=c
    heapq.heappush(arr, c)

print(cost)
