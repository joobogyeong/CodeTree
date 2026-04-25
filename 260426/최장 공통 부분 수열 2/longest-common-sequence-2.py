A = input()
B = input()

len_A = len(A)
len_B = len(B)

dp = [[0 for _ in range(len_B + 1)] for _ in range(len_A + 1)]

def initialization():
    for i in range(1, len_A + 1):
        if A[i - 1] == B[0]:
            dp[i][1] = 1
        else:
            dp[i][1] = dp[i - 1][1]

    for j in range(1, len_B + 1):
        if B[j - 1] == A[0]:
            dp[1][j] = 1
        else:
            dp[1][j] = dp[1][j - 1]

initialization()

for i in range(2, len_A + 1):
    for j in range(2, len_B + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#backtracking으로 구하기
i = len_A
j = len_B
result = []

while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
        result.append(A[i - 1])
        i -= 1
        j -= 1
    else:
        if dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

result.reverse()
print(''.join(result))