MAX_M = 3
MOD = 10007
n = int(input())
dp = [0 for _ in range(n+1)]
numbers = [1, 2, 5]

dp[0] = 1

for i in range(1, n+1):
    for j in range(MAX_M):
        if i >= numbers[j]:
            dp[i] = (dp[i]+dp[i-numbers[j]])%MOD

print(dp[n])