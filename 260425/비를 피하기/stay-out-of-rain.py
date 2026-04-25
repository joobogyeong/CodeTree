from collections import deque
N, H, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
result_grid=[[0]*N for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def in_range(x, y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

def can_go(x, y):
    if in_range(x, y)==False or visited[x][y]==True or grid[x][y]==1:
        return False
    else:
        return True

def bfs(start_x, start_y):
    visited = [[False]*N for _ in range(N)]
    q=deque()
    q.appendleft((start_x, start_y, 0))
    visited[start_x][start_y]=True
    while q:
        x, y, d = q.pop()
        if grid[x][y]==3:
            return d
        for ix, iy in zip(dx, dy):
            new_x=x+ix
            new_y=y+iy
            if in_range(new_x, new_y)==True and visited[new_x][new_y]==False and grid[new_x][new_y]!=1:
                visited[new_x][new_y]=True
                q.appendleft((new_x, new_y, d+1))
    return -1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            result_grid[i][j] = bfs(i, j)

for row in result_grid:
    print(*row)