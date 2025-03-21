N, T = map(int,input().split())
array=list(map(int, input().split()))
cnt=0
max_cnt=0
for i in range(N):
    if (i==0 and array[i]>T) or (array[i]>T and array[i]>array[i-1]):
        cnt+=1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt=1
print(max(max_cnt, cnt))