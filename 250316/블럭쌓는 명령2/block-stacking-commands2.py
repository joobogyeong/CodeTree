N, k = map(int, input().split())
block = []
for _ in range(k):
    block.append(tuple(map(int, input().split())))

# 블록 결과 리스트 초기화
block_result = [0] * (N + 1)

# 블록 개수를 센다
for i in range(k):
    for j in range(block[i][0], block[i][1] + 1):
        block_result[j] += 1

# 최댓값 출력
print(max(block_result))
