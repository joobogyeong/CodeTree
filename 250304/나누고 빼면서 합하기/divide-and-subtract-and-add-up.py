n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def func(n, m):
    sum=0
    while m>0:
        if m%2==0:
            sum+=A[m-1]
            m//=2
        else:
            sum+=A[m-1]
            m-=1
    return sum

print(func(n, m))