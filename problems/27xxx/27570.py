import sys
from collections import deque

def solve_cookie_problem():
    input = sys.stdin.readline

    try:
        n, m = map(int, input().split())
        grid = [input().strip() for _ in range(n)]
    except (IOError, ValueError):
        print(0)
        return

    dist = [[-1] * m for _ in range(n)]
    q = deque()
    max_dist = 0

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'X':
                is_exposed = False
                if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                    is_exposed = True
                else:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if grid[r + dr][c + dc] == '-':
                            is_exposed = True
                            break
                
                if is_exposed:
                    dist[r][c] = 1
                    q.append((r, c))
                    max_dist = 1
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'X' and dist[nr][nc] == -1:
                new_distance = dist[r][c] + 1
                dist[nr][nc] = new_distance
                q.append((nr, nc))
                
                if new_distance > max_dist:
                    max_dist = new_distance

    print(max_dist)

if __name__ == "__main__":
    solve_cookie_problem()