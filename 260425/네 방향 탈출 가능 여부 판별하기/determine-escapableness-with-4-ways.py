from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def bfs():
    while q:
        x, y = q.pop()

        for ix, iy in zip(dx, dy):
            new_x = x + ix
            new_y = y + iy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.appendleft((new_x, new_y))

if grid[0][0] == 1:
    q.appendleft((0, 0))
    visited[0][0] = True
    bfs()

if visited[N - 1][M - 1]:
    print(1)
else:
    print(0)