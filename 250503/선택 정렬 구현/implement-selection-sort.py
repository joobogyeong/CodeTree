n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]  # swap

for elem in arr:
    print(elem, end=" ")
