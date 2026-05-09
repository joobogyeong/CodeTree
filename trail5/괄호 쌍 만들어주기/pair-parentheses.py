A = input()
length = len(A)

checked = [0] * length

for i in range(length-2, -1, -1):
    checked[i] = checked[i+1]
    if A[i] == ')' and A[i+1] == ')':
        checked[i] += 1
        
answer = 0
for i in range(0, length-4):
    if A[i] == '(' and A[i+1]=='(':
        answer += checked[i]

print(answer)