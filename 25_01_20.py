N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()
def dfs(start_node,visited = []):
    visited.append(start_node)
    print(start_node, end=' ')

    for node in graph[start_node]:
        if node not in visited:
            dfs(node,visited)
def bfs(start_node,visited = []):
    from collections import deque
    queue = deque([start_node])
    visited.append(start_node)

    while queue:
        visit = queue.popleft()
        print(visit, end=' ')
        for i in graph[visit]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

dfs(V)
print()
bfs(V)


















# def make_graph(NMV, nodes):
#     dict = {}
#     for i in range(NMV[0]):
#         dict[i+1] = 0
#
#     for i in nodes:
#         if dict[i[0]] == 0:
#             dict[i[0]] = [i[1]]
#             dict[i[1]] = [i[0]]
#         else:
#             tmp_i = dict[i[0]]
#             tmp_i.append(i[1])
#             dict[i[0]] = tmp_i
#             tmp_j = dict[i[1]]
#             tmp_j.append(i[0])
#             dict[i[1]] = tmp_j
#     return dict
#
# graph = make_graph(NMV,nodes)