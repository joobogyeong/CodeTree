import sys

INT_MIN = -sys.maxsize

n, m = tuple(map(int, input().split()))
coin = [0] + list(map(int, input().split()))
dp = [0 for _ in range(m+1)]

def initialization():
    for i in range(m+1):
        dp[i]=INT_MIN
        dp[0]=0
initialization()

for i in range(1, m+1):
    for j in range(1, n+1):
        if i>=coin[j]:
            if dp[i-coin[j]]==INT_MIN:
                continue
            dp[i] = max(dp[i], dp[i-coin[j]]+1)

ans = dp[m]
if ans == INT_MIN:
    ans = -1

print(ans)
