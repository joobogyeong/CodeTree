from collections import deque
N = int(input())
arr = list(map(int, input().split()))
start = (arr[0], arr[1])
end = (arr[2], arr[3])
visited = [[False]*N for _ in range(N)]
q=deque()

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def in_range(x, y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

def can_go(x, y):
    if in_range(x, y)==False or visited[x][y]==True:
        return False
    else:
        return True

def bfs():
    
    while q:
        x, y, d = q.pop()

        if x == end[0]-1 and y == end[1]-1:
            return d

        for ix, iy in zip(dx, dy):
            new_x = x+ix
            new_y = y+iy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.appendleft((new_x, new_y, d+1))
    return -1

visited[start[0]-1][start[1]-1]=True
q.appendleft((start[0]-1, start[1]-1, 0))
print(bfs())