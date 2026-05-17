N, M = map(int, input().split())
arr = list(map(int, input().split()))

def BS(arr, target):
    left = 0
    right = len(arr)-1
    while(left<=right):
        mid = (left + right) // 2
        if arr[mid]==target:
            return mid+1
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for _ in range(M):
    target = int(input())
    result = BS(arr, target)
    print(result)
    