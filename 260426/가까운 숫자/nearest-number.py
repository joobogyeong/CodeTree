from sortedcontainers import SortedSet

N = int(input())
arr = list(map(int, input().split()))

ss = SortedSet()
shortest_len = float('inf')

ss.add(0)

for elem in arr:
    index = ss.bisect_left(elem)

    minner_len = float('inf')

    # 왼쪽 이웃
    if index > 0:
        l_len = elem - ss[index - 1]
        minner_len = min(minner_len, l_len)

    # 오른쪽 이웃
    if index < len(ss):
        r_len = ss[index] - elem
        minner_len = min(minner_len, r_len)

    ss.add(elem)
    shortest_len = min(shortest_len, minner_len)

    print(shortest_len)