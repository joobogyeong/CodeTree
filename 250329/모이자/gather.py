N=int(input())
array=list(map(int, input().split()))
length=0
min_length=0
for i in range(N):
    length=0
    for j in range(N):
        length+=array[j]*abs(i-j)
    if i==0:
        min_length=length
    if min_length>=length:
        min_length=length
print(min_length)