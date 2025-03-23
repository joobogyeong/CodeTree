N, M = map(int, input().split())

move_A = [
    tuple(input().split())
    for _ in range(N)
]
move_B = [
    tuple(input().split())
    for _ in range(M)
]

current_A_index = 0
current_B_index = 0

array_A = []
array_B = []

for i in range(N):
    if move_A[i][0]=="R":
        for _ in range(int(move_A[i][1])):
            current_A_index+=1
            array_A.append(current_A_index)
    else:
        for _ in range(int(move_A[i][1])):
            current_A_index-=1
            array_A.append(current_A_index)

for i in range(M):
    if move_B[i][0]=="R":
        for _ in range(int(move_B[i][1])):
            current_B_index+=1
            array_B.append(current_B_index)
    else:
        for _ in range(int(move_B[i][1])):
            current_B_index-=1
            array_B.append(current_B_index)

for i in range(len(array_A)):
    if array_A[i]==array_B[i]:
        print(i+1)
        break
else:
    print(-1)
    


