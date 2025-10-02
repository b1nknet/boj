import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
price = [list(map(int, input().rstrip())) for _ in range(N)]

DP = defaultdict(list)

DP[1] = [[0] * 10 for _ in range(N)]


def DFS(visit, s, p):
    if DP[visit] == []:
        DP[visit] = [[0] * 10 for _ in range(N)]
    
    if DP[visit][s][p] != 0:
        return DP[visit][s][p]
    
    cnt = 0
    for i in range(N):
        if visit & 1 << i == 0:
            if p <= price[s][i]:
                cnt = max(cnt, DFS(visit | 1 << i, i, price[s][i]) + 1)
    
    DP[visit][s][p] = cnt
    return cnt

print(DFS(1, 0, 0) + 1)