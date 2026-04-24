from collections import deque
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
start_point = [list(map(int, input().split())) for _ in range(K)]

q=deque()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 0

def bfs():
    while q:
        x, y = q.pop()

        for ix, iy in zip(dx, dy):
            new_x = x + ix
            new_y = y + iy

            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.appendleft((new_x, new_y))

for x, y in start_point:
    x-=1
    y-=1

    if can_go(x, y):
        visited[x][y]=True
        q.appendleft((x, y))
    
bfs()

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]==True:
            cnt+=1
print(cnt)