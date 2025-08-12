from collections import deque
n=int(input())
dq=deque()

for i in range(1, n+1):
    dq.append(i)

for _ in range(n-1):
    dq.popleft()
    x=dq.popleft()
    dq.append(x)

print(dq.pop())




