A = input()

# Please write your code here.

def fun(a):
    lena=len(a)
    for i in range(lena-1):
        if a[i]!=a[i+1]:
            return True
    return False

if fun(A):
    print("Yes")
else:
    print("No")
