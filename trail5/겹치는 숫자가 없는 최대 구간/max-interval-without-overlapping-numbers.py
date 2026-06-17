import sys

N = int(input())
arr = list(map(int, input().split()))
max_len = -sys.maxsize
count_arr = [0]*100001
j = 0
ans = 0
for i in range(N):
    while j<=N-1 and count_arr[arr[j]]!=1:
        count_arr[arr[j]]+=1
        j+=1
    ans = max(ans, j - i)
    count_arr[arr[i]]-=1
print(ans)
    