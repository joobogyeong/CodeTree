from sortedcontainers import SortedDict
N = int(input())
sd = SortedDict()

line = [input().split() for _ in range(N)]

def add(k, v):
    sd[k] = v

def remove(k):
    sd.pop(k, None)

def find(k):
    if k in sd:
        print(sd[k])
    else:
        print("None")
def print_list():
    if len(sd)==0:
        print("None")
    else:
        for value in sd.values():
            print(value, end=" ")
        print()

for i in range(N):
    if line[i][0] == "add":
        add(int(line[i][1]), int(line[i][2]))
    elif line[i][0] == "remove":
        remove(int(line[i][1]))
    elif line[i][0] == "find":
        find(int(line[i][1]))
    else:
        print_list()