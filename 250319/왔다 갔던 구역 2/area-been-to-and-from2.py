N=int(input())
arr=[
    tuple(input().split())
    for _ in range(N)
]
result_array=[0]*1000
current_point=500
for i in range(N):
    if arr[i][1]=='R':
        for _ in range(int(arr[i][0])):
            result_array[current_point]+=1
            current_point+=1
    else:
        for _ in range(int(arr[i][0])):
            result_array[current_point]+=1
            current_point-=1
cnt=0
for elem in result_array:
    if int(elem)>=2:
        cnt+=1
print(cnt)