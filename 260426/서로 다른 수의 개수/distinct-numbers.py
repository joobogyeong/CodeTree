N = int(input())
arr = list(map(int, input().split()))
set = set(arr)
cnt = 0
for elem in set:
    cnt+=1

print(cnt)