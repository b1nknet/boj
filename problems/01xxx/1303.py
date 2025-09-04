input = __import__('sys').stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    q = deque() 
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and array[nx][ny] == color:
                    visited[nx][ny] = True 
                    q.append((nx ,ny))
                    count += 1 
    return count 

m, n = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(input()))

visited = [[False] * m for _ in range(n)]

blue = 0
white = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 'B':
            blue += bfs(i, j, array[i][j]) ** 2
        elif not visited[i][j] and array[i][j] == 'W':
            white += bfs(i, j, array[i][j]) ** 2

print(white, blue)
