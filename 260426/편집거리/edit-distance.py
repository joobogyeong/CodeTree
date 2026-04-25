str1 = input()
str2 = input()

str1_len, str2_len = len(str1), len(str2)
str1, str2 = '#' + str1, '#' + str2

dp = [
    [0 for _ in range(str2_len + 1)]
    for _ in range(str1_len + 1)
]

def initialize():
    dp[0][0] = 0
    
    for i in range(1, str1_len + 1):
        dp[i][0] = i
    
    for j in range(1, str2_len + 1):
        dp[0][j] = j
            
initialize()

for i in range(1, str1_len + 1):
    for j in range(1, str2_len + 1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1]
        
        else:
            dp[i][j] = min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1
            
print(dp[str1_len][str2_len])
