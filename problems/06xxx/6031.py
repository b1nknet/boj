from collections import deque

def bfs(y, x, t):
    q = deque()
    q.append((y, x))
    graph[y][x] = t
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < H) and (0 <= X < W) and graph[Y][X] == '.':
                q.append((Y, X))
                graph[Y][X] = t
    return cnt
    
W, H = map(int, input().split())
graph = [list(input()) for _ in range(H)]
d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
cnt, res = 1, 0
for i in range(H):
    for j in range(W):
        if graph[i][j] == '.':
            res = max(res, bfs(i, j, cnt))
            cnt += 1
print(res)