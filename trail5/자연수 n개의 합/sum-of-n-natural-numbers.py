S = int(input())

left = 1
right = S
min_idx = S+1

while left <= right:
    mid = (left + right) // 2
    if mid  * (mid + 1) // 2 > S:
        right = mid - 1
        min_idx = min(min_idx, mid)
    else:
        left = mid + 1

print(min_idx-1)