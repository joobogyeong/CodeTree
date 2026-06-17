N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
count = 0
j = 0
for i in range(N):
    while j < N and sum < M:
        sum+=arr[j]
        j+=1
    if sum==M:
        count+=1
        
    sum-=arr[i]

print(count)