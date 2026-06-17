from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

N = int(input())
nums = []
for _ in range(N):
    num = input()
    nums.append(num)

result = sorted(nums, key=cmp_to_key(compare))

for elem in result:
    print(elem, end="")
