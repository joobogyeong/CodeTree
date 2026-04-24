import sys
sys.setrecursionlimit(10**6)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

area = 0
max_cnt = 0

def in_range(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False

def can_go(x, y):
    if in_range(x, y) and not visited[x][y]:
        return True
    else:
        return False

def dfs(x, y):
    cnt = 1
    visited[x][y] = True

    for nx, ny in zip(dx, dy):
        new_x = x + nx
        new_y = y + ny

        if can_go(new_x, new_y) and grid[x][y] == grid[new_x][new_y]:
            cnt += dfs(new_x, new_y)

    return cnt

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt = dfs(i, j)

            if cnt >= 4:
                area += 1

            max_cnt = max(max_cnt, cnt)

print(area, max_cnt)