N = int(input())
memo = [-1] * (N+1)

def dp(n):
    if memo[n]!=-1:
        return memo[n]
    elif n==1:
        memo[n]=1
    elif n==2:
        memo[n]=2
    else:
        memo[n]=dp(n-1)+dp(n-2)
    return memo[n]

print(dp(N)%10007)