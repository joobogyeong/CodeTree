N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

left = 1
right = max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2

    count = 0
    for num in arr:
        count += num // mid

    if count >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)