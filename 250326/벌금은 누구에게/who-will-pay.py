N, M, K = map(int, input().split())
array_student = [
    int(input())
    for _ in range(M)
]
array_penalty = [0]*N

for elem in array_student:
    array_penalty[elem-1]+=1
    if array_penalty[elem-1]==K:
        print(elem)
        break
else:
    print(-1)