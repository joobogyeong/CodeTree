import sys

input = sys.stdin.readline

n, m = map(int, input().split())

segments = []

for _ in range(m):
    a, b = map(int, input().split())
    segments.append((a, b))

segments.sort()


def possible(dist):
    count = 0
    last = -10**30

    for left, right in segments:
        start = max(left, last + dist)

        if start > right:
            continue

        can_place = (right - start) // dist + 1
        count += can_place

        last = start + (can_place - 1) * dist

        if count >= n:
            return True

    return False


answer = 0
low = 1
high = 10**18

while low <= high:
    mid = (low + high) // 2

    if possible(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)