N=int(input())
arr=[]
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
line = [0]*101
for a,b in arr:
    for j in range(a, b+1):
        line[j]+=1
print(max(line))


