A, B = map(int,input().split())
N=input()
N=list(N)
num=0
for i in range(len(N)):
    num=num*A+int(N[i])
digit=[]
while True:
    if num<B:
        digit.append(num)
        break
    digit.append(num%B)
    num//=B
for elem in digit[::-1]:
    print(elem, end='')
