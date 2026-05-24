# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
jewels = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = 0

jewels.sort(key=lambda x: -x[1] / x[0])

for w, v in jewels:
    if m >= w:
        m -= w
        ans += v
    else:
        ans += m / w * v
        break

print(f"{ans:.3f}")
