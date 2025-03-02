A = input()

# Please write your code here.

def pal(A):
    if A==A[-1::-1]:
        return(True)
    else:
        return(False)
    
if pal(A)==True:
    print("Yes")
else:
    print("No")