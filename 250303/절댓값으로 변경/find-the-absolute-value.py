n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def _abs(arr):
    for i in range(n):
        if arr[i]<0:
            arr[i]*=-1
    
_abs(arr)
for elem in arr:
    print(elem, end=' ')
