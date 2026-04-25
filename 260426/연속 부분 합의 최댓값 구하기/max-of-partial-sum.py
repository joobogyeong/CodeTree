import sys

N = int(input())
arr = list(map(int, input().split()))
MIN_INT = -sys.maxsize

dp = [MIN_INT] * N

dp[0] = arr[0]

for i in range(N):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))