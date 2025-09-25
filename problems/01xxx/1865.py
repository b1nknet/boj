import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start,n):
    dist = [INF for i in range(n + 1)]
    dist[start] = 0
    for i in range(n):
        for s,e,t in graph:
            if dist[e] > dist[s] + t:
                if i == n - 1:
                    return True
                dist[e] = dist[s] + t
    return False

tc = int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    graph = []
    for i in range(m):
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for i in range(w):
        s,e,t = map(int,input().split())
        graph.append((s,e,-t))

    tf = bellman_ford(1,n)

    if tf == True:
        print("YES")
    else:
        print("NO")