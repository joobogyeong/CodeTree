from collections import deque
n=int(input())
dq=deque()

for 1 in range(n+1):
    dq.append(i)

for _ in range(n-1):
    dq.popleft()
    x=dq.popleft()
    dq.append(x)

print(dq)




