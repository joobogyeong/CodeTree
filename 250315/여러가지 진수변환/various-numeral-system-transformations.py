N, B=map(int,input().split())

digit=[]
if B==4:
    digit=[]
    while True:
        if N<4:
            digit.append(N)
            break
        digit.append(N%4)
        N//=4
else:
    digit=[]
    while True:
        if N<8:
            digit.append(N)
            break
        digit.append(N%8)
        N//=8

for elem in digit[::-1]:
    print(elem, end='')
