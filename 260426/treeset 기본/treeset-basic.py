# bisect는 **O(logN)** 시간복잡도라 강력하다.left right는 방향의 차이.
# index를 반환하는거임
from sortedcontainers import SortedSet

N = int(input())
ss= SortedSet()

for _ in range(N):
    line = input().split()
    if line[0]=='add':
        ss.add(int(line[1]))
    elif line[0]=='remove':
        ss.remove(int(line[1]))
    elif line[0]=='find':
        if int(line[1]) in ss:
            print("true")
        else: 
            print("false")
    elif line[0]=='lower_bound':
        index = ss.bisect_left(int(line[1]))
        if index < len(ss):
            print(ss[index])
        else:
            print('None')
    elif line[0]=='upper_bound':
        index = ss.bisect_right(int(line[1]))
        if index < len(ss):
            print(ss[index])
        else:
            print('None')
    elif line[0]=='largest':
        if ss:
            print(ss[-1])
        else:
            print('None')
    elif line[0]=='smallest':
        if ss:
            print(ss[0])
        else:
            print('None')

