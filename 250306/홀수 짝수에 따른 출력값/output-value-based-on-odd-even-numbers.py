N=int(input())

def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n%2==0:
        return n+f(n-2)
    else:
        return n+f(n-2)

print(f(N))