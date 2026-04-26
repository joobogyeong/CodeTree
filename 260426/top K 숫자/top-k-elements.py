from sortedcontainers import SortedSet

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ss = SortedSet(arr)
cnt = 0
for elem in ss[-1: :-1]:
    if cnt == K:
        break
    else:
        print(elem, end=" ")
        cnt+=1


