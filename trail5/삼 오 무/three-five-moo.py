N = int(input())

left = 1
right = N * 2
answer = 0

while left <= right:
    mid = (left + right) // 2

    count = mid - mid // 3 - mid // 5 + mid // 15

    if count >= N:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)