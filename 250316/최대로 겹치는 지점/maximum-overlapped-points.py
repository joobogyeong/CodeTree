N=int(input())
a=[]
for _ in range(N):
    a.append(tuple(map(int, input().split())))
line = [0]*200
for a,b in a:
    for j in range(a+100, b+100):
        line[j]+=1
print(max(line))


