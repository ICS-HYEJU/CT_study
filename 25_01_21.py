import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start,visited):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(v,visited)

graph_cnt = 0
visited = [False] * (N+1)
for i in range(1,N+1):
    if not visited[i]:
        dfs(i,visited)
        graph_cnt += 1
print(graph_cnt)
