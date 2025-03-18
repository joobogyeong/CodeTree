N=int(input())
arr=[
    tuple(input().split())
    for _ in range(N)
]
result_array=[0]*2000
current_point=1000
for i in range(N):
    if arr[i][1]=='R':
        for _ in range(int(arr[i][0])):
            result_array[current_point]+=1
            current_point+=1
    else:
        for _ in range(int(arr[i][0])):
            result_array[current_point]+=1
            current_point-=1

cnt = sum(1 for visits in result_array if visits >= 2)
print(cnt)