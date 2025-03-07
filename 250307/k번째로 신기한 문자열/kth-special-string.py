n, k, t = input().split()
n, k = int(n), int(k)
string = [input() for _ in range(n)]

# Please write your code here.
string.sort()
new_str=[]
for i in range(n):
    if t in string[i]:
        new_str.append(string[i])

print(new_str[k-1])