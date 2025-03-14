digit=list(map(int, input().split()))
num=0
for i in range(len(digit)):
    num = num*2 + digit[i]
print(num)