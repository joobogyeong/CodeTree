n = int(input())
arr = list(map(int, input().split()))

answer = 0

def flip(idx):
    if 0 <= idx < n:
        arr[idx] = 1 - arr[idx]

for i in range(n - 1):
    if arr[i] == 0:
        flip(i)
        flip(i + 1)
        flip(i + 2)
        answer += 1

if arr[n - 1] == 1:
    print(answer)
else:
    print(-1)