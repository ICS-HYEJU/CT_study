from collections import deque
N,K = map(int, input().split())
max = 10**5
visited = [0] * (max+1)

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            print(visited[x])
            break
        for next_x in (x-1, x+1, 2*x):
            if (0 <= next_x <= max) and not visited[next_x]:
                visited[next_x] = visited[x] + 1
                queue.append(next_x)
bfs()