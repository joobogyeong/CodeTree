N, K = map(int,input().split())
arr=list(map(int, input().split()))

sorted_arr=sorted(arr)
print(sorted_arr[K-1])