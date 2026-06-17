n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
num = 0

for i in range(n-1, -1, -1):
    n = k // coins[i]
    num = num + n
    k = k % coins[i]

print(num)
    
