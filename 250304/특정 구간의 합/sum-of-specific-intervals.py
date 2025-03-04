n,m = map(int, input().split())
A=list(map(int, input().split()))
ssang = [tuple(map(int, input().split()))for _ in range(m)]

def func():
    global A
    for i in range(m):
        sum=0
        for j in range(ssang[i][0]-1,ssang[i][1]):
            sum+=A[j]
        print(sum)

func()