n, k = map(int, input().split())

points = []
cur = 0

for _ in range(n):
    length, direction = input().split()
    length = int(length)

    if direction == 'R':
        next_pos = cur + length
    else:
        next_pos = cur - length

    start = min(cur, next_pos)
    end = max(cur, next_pos)

    points.append((start, 1))
    points.append((end, -1))

    cur = next_pos

points.sort()

answer = 0
count = 0

for i in range(len(points) - 1):
    x, value = points[i]
    count += value

    next_x = points[i + 1][0]

    if count >= k:
        answer += next_x - x

print(answer)