N=int(input())
def sum_1_n(n):
    if n==0:
        print()
        return
    sum_1_n(n-1)
    print(n, end=' ')

def sum_n_1(n):
    if n==0:
        print()
        return
    print(n, end=' ')
    sum_n_1(n-1)

sum_1_n(N)
sum_n_1(N)
    
