N = int(input())
d = {}
cmd = []

line = [list(input().split()) for _ in range(N)]


def add(k, v):
    d[k]=v
def remove(k):
    d.pop(k)
def find(k):
    if k in d:
        print(d[k])
    else:
        print("None")

for i in range(N):
    if line[i][0] == "add":
        add(line[i][1], line[i][2])
    elif [i]=="remove":
        remove(line[i][1])
    elif cmd[i]=="find":
        find(line[i][1])