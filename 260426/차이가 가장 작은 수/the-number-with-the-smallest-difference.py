import sys
from sortedcontainers import SortedSet

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]

s = SortedSet(arr)
ans = INT_MAX


for x in arr:
    min_idx = s.bisect_left(m + x)
    if min_idx != len(s):
        ans = min(ans, s[min_idx] - x)
    max_idx = s.bisect_right(x - m) - 1
    if max_idx >= 0:
        ans = min(ans, x - s[max_idx])

if ans == INT_MAX:
    ans = -1

print(ans)
