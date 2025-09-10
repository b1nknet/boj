input = __import__('sys').stdin.readline
from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_rain = max(map(max, graph))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(i,j):
    global count
    q = deque()
    q.append((i,j))
    sink[i][j] = True
    count += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny < 0 or nx >= N or ny >= N:
                continue
            if sink[nx][ny]==False:
                sink[nx][ny] = True
                q.append((nx,ny))
count_list = []
for rain in range(max_rain):
    count = 0
    sink = [[False for _ in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j]<=rain:
                sink[i][j]=True
    for i in range(N):
        for j in range(N):
            if sink[i][j]==False:
                bfs(i,j)
    count_list.append(count)

print(max(count_list))