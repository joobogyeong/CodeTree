N=int(input())
a=[]
for _ in range(N):
    a.append(tuple(map(int, input().split())))
line = [0]*100
for A,b in a:
    for j in range(A, b+1):
        line[j]+=1
print(max(line))


