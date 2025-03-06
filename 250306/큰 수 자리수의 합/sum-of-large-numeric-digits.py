a, b, c = map(int, input().split())
sum=a*b*c
def f(n):
    if n<10:
        return n
    return f(n//10)+n%10

print(f(sum))

