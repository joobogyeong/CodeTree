n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(a, b, n1, n2):
    found=False
    for i in range(n1-n2+1):
        if a[i]==b[0]:
            for j in range(n2):
                if a[i+j]==b[j]:
                    found = True
                else: 
                    found = False
                    break
        if found:
            return True
    return False

result=func(a,b,n1,n2)
if result:
    print("Yes")
else:
    print("No")

