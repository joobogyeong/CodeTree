OFFSET = 100  # 좌표를 0 이상으로 변환하기 위한 값
GRID_SIZE = 201  # -100 ~ 100이므로, 총 크기는 201 x 201

# 2차원 평면을 0으로 초기화
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# 입력
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    # 좌표를 0 이상으로 변환
    x1 += OFFSET
    x2 += OFFSET
    y1 += OFFSET
    y2 += OFFSET

    # 직사각형을 grid에 표시
    for x in range(x1, x2):  # x2 포함 안 함
        for y in range(y1, y2):  # y2 포함 안 함
            grid[x][y] = 1  # 직사각형이 차지하는 부분을 1로 설정

# 총 넓이 계산
total_area = sum(sum(row) for row in grid)
print(total_area)
