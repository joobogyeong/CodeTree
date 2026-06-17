n = int(input())
start = input().strip()
target = input().strip()

answer = 0
flipped = False

for i in range(n - 1, -1, -1):
    current = start[i]

    if flipped:
        current = 'H' if current == 'G' else 'G'

    if current != target[i]:
        answer += 1
        flipped = not flipped

print(answer)