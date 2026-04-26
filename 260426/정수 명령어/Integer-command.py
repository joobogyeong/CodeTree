from sortedcontainers import SortedSet

T = int(input())
s = SortedSet()

for i in range(T):
    s.clear()
    K = int(input())
    for j in range(K):
        cmd = input().split()
        if cmd[0]=="I":
            s.add(int(cmd[1]))
        if s:
            if cmd[0]=="D" and cmd[1]=='1':
                s.remove(s[-1])
            elif cmd[0]=="D" and cmd[1]=='-1':
                s.remove(s[0])
        else:
            continue
    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])