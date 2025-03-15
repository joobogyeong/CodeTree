N, k = map(int, input().split())
block=[]
for _ in range(k):
    block.append(tuple(map(int,input().split())))
block_result=[0]*(N+1)
for i in range(k):
    for j in range(block[i][0],block[i][1]+1):
        block_result[j]+=1
print(max(block_result))
