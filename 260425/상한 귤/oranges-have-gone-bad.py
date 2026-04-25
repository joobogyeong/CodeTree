from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
step = [[-1]*N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
q = deque()

def in_range(x, y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

def can_go(x, y):
    if  in_range(x, y) and grid[x][y]==1 and visited[x][y]==False:
        return True
    else:
        return False

def bfs():
    while q:
        x, y = q.popleft()
        for nx, ny in zip(dx, dy):
            new_x = nx + x
            new_y = ny + y
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                step[new_x][new_y] = step[x][y]+1
                q.append((new_x, new_y))

for i in range(N):
    for j in range(N):
        if grid[i][j]==1 or grid[i][j]==2:
            step[i][j]=-2

for i in range(N):
    for j in range(N):
        if grid[i][j]==2:
            visited[i][j]=True
            step[i][j]=0
            q.append((i, j))

bfs()
for row in step:
    print(*row)
