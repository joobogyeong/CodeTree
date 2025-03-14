binary=list(map(int, input().strip()))
num=0
for i in range(len(binary)):
    num = num*2 + binary[i]
print(num)