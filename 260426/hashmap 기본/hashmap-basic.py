N = int(input())
d = {}

for i in range(N):
    cmd = list(input().split())
    if cmd[0]=='add':
        d[int(cmd[1])]=int(cmd[2])
    elif cmd[0]=='remove':
        d.pop(int(cmd[1]))
    elif cmd[0]=='find':
        if int(cmd[1]) in d:
            print(d[int(cmd[1])])
        else:
            print('None')


