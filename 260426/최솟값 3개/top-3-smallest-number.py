import heapq
N = int(input())
arr = list(map(int, input().split()))
h=[]
for elem in arr:
    heapq.heappush(h, elem)
    if len(h)<3:
        print(-1)
    else:
        cross = 1
        
        num1 = heapq.heappop(h)
        num2 = heapq.heappop(h)
        num3 = heapq.heappop(h)
        cross = num1*num2*num3 
        print(cross)
        heapq.heappush(h, num1)
        heapq.heappush(h, num2)
        heapq.heappush(h, num3)











