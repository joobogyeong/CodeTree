N=int(input())
array=[
    int(input())
    for _ in range(N)
]
cnt=0
max_cnt=0
for i in range(N):
    if i==0 or array[i]==array[i-1]:
        cnt+=1
    else:
        if max_cnt < cnt:
            cnt+=1
            max_cnt = cnt
            cnt=0
print(max_cnt)