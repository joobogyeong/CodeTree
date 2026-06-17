N, M = map(int, input().split())

points = []
for _ in range(N):
    points.append(int(input()))

points.sort()

left = 1
right = points[-1] - points[0]
answer = 0

while left <= right:
    mid = (left + right) // 2

    count = 1
    last = points[0]

    for i in range(1, N):
        if points[i] - last >= mid:
            count += 1
            last = points[i]

    if count >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)