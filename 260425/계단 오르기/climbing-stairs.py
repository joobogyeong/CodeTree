N = int(input())
memo = [-1]*(N+1)

def dp(n):
    if memo[n]!=-1:
        return memo[n]
    if n==2 or n==3:
        memo[n]=1
    elif n==1 or n==0:
        memo[n]=0
    else:
        memo[n]=dp(n-2)+dp(n-3)
    return memo[n]

dp(N)
if memo[N]==-1:
    print(0)
else:
    print(memo[N]%10007)