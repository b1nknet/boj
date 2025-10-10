from collections import deque
import sys

input = sys.stdin.readline
MAX_SIZE = 100001

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [-1] * MAX_SIZE
visited[n] = 0

min_cnt = 0;

while q:
  now = q.popleft()

  if now == k :
    min_cnt += 1

  for next in [now + 1, now - 1, now * 2]:
    if 0 <= next < MAX_SIZE:
      if visited[next] == -1 or visited[next] >= visited[now] + 1:
        visited[next] = visited[now] + 1
        q.append(next)

print(visited[k])
print(min_cnt)