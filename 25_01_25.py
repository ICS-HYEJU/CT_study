from collections import deque
N,K = map(int,input().split())
max = 10**5
min_sec = 10**5
visited = [0]*(max+1)
cnt = 0

def bfs():
    global min_sec,cnt
    queue = deque()
    queue.append(N)
    # 5 10 9 18 17
    # 5 4 8 16 17
    while queue:
        x = queue.popleft()
        if x == K:
            cnt += 1
            min_sec = min(min_sec,visited[x])
            continue

        for next_x in (x-1,x+1,2*x):
            if (0<= next_x <=max) and (not visited[next_x] or visited[next_x]>=visited[x]+1):
                queue.append(next_x)
                visited[next_x] = visited[x] + 1
bfs()
print(min_sec)
print(cnt)
