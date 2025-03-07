N=int(input())
arr=list(map(int, input().split()))

for i in range(1,len(arr)+1):
    sorted_arr=[]
    for j in range(i):
        sorted_arr.append(arr[j])
    sorted_arr.sort()
    if i%2==1:
        print(sorted_arr[i//2], end=" ")