N=int(input())
digit=[]
while True:
    digit.append(N%2)
    N//=2
    if N<2:
        digit.append(N)
        break
for elem in digit[::-1]:
    print(elem, end='')