#집함ㅂㅂ
N = int(input())
s=set()
for _ in range(N):
    line = list(input().split())
    if line[0]=='add':
        s.add(line[1])
    elif line[0]=='remove:
        s.remove(line[1])
    else:
        if line[1] in s:
            print("true")
        else:
            print("false")



