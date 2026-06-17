N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
point = []
for i in range(N):
    point.append((arr[i][0], +1, i))
    point.append((arr[i][1], -1, i))

point.sort()
sets = set()
ans = 0

for x, v, index in point:
    if v == +1:
        if len(sets)==0:
            ans+=1
        sets.add(index)
    else:
        sets.remove(index)

print(ans)


