import sys
N = int(input())
line = [tuple(map(int, input().split())) for _ in range(N)]
max_sum = -sys.maxsize
sum = 0
checked = [0] * 200001

for x1, x2 in line:
    checked[x1]+=1 
    checked[x2]-=1

for num in checked:
    sum += num
    max_sum = max(max_sum, sum)

print(max_sum)