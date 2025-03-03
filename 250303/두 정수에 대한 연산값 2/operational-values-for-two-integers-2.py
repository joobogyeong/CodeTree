a, b =map(int, input().split())

def fun(a, b):
    if a<b:
        b*=2
        a+=10
    else:
        a*=2
        b+=10
    return a, b

A, B = fun(a, b)
print(f"{A} {B}")