n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()
new_str=[]
for i in range(n):
    if t in str[i]:
        new_str.append(str[i])

print(new_str[k-1])