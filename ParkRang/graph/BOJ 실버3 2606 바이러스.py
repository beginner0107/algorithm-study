import sys
# 노드
V = int(sys.stdin.readline())
# 간선
E = int(sys.stdin.readline())

# 그래프
graph = [[] for _ in range(V + 1)]
for _ in range(E) :
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

# dfs
def dfs(graph, visited, node) :
    visited[node] = True
    cnt = 1
    # 수행 동작
    for g in graph[node] :
        if not visited[g] :
            cnt = cnt + dfs(graph, visited, g)
    return cnt

visited = [False] * (V + 1)
print(dfs(graph, visited, 1) -1)
