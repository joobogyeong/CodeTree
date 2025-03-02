a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    if a>b:
        a+=25
        b*=22
        return a, b
    else:
        b+=25
        a*=2
        return a, b
a, b = fun(a,b)
print(f"{a} {b}")