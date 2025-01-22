import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

result = []
def dfs(x,y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if graph[x][y] == 1:
        cnt+=1
        graph[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                dfs(nx,ny)

cnt = 0
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            dfs(x,y)
            result.append(cnt)
            cnt = 0
result.sort()
print(len(result))
for i in result:
    print(i)