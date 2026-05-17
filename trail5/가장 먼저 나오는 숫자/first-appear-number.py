N, M = map(int, input().split())
arr = list(map(int, input().split()))
ask = list(map(int, input().split()))

def BS(target):
    left = 0
    right = N - 1
    min_idx = N

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    if min_idx == N:
        return -1

    if arr[min_idx] != target:
        return -1

    return min_idx + 1


for elem in ask:
    print(BS(elem))