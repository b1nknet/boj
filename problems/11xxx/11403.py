import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
#Floyd-Warshall - 모든 정점에 대한 경로 계산
for k in range(N):
    for i in range(N):
        for j in range(N): 
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()