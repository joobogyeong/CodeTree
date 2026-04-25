from sortedcontainers import SortedDict
N = int(input())
sd = SortedDict()

for _ in range(N):
    color = input()
    if  color not in sd:
        sd[color]=1
    else:
        sd[color]+=1

for color, num in sd.items():
    print(f"{color} {100/N*num:.4f}")