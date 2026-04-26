A, B = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
set_A = set(arr_A)
set_B = set(arr_B)
set_new_A = set()
for elem in set_A:
    if elem in set_B:
        set_B.remove(elem)
    else:
        set_new_A.add(elem)

print(len(set_new_A)+len(set_B))
