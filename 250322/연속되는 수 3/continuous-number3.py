N=int(input())
array=[
    int(input())
    for _ in range(N)
]
cnt=0
max_cnt=0
for i in range(N):
    if i==0 or array[i]*array[i-1]>0:
        cnt+=1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt=1
print(max(max_cnt, cnt))