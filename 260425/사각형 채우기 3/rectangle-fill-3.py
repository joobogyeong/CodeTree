N = int(input())
memo = [-1] * (N+1)

def dp(n):
    if memo[n]!=-1:
        return memo[n]
    elif n==1:
        memo[n]=2
    elif n==2:
        memo[n]=7
    elif n==3:
        memo[n]=22    
    else:
        memo[n]=2*(dp(n-1))+3*(dp(n-2))+2*(dp(n-3))
    return memo[n]

print(dp(N)%1000000007)