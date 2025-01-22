import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(r,c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if (0 <= nx < M) and (0 <= ny < N) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx,ny)

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        graph[r][c] = 1

    count = 0
    for c in range(M):
        for r in range(N):
            if graph[r][c] == 1:
                dfs(c,r)
                count += 1
    print(count)