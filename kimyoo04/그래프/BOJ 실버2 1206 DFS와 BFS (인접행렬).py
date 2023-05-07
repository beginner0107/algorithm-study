# https://www.acmicpc.net/problem/1260

"""
핵심
- DFS, BFS
- 인접행렬, 인접리스트
- 재귀함수
- sys.setrecursionlimit(100000)
"""

import sys; input=sys.stdin.readline; sys.setrecursionlimit(100000)
from collections import deque

# N: 정점의 개수, M: 간선의 개수, V: 시작 정점의 번호
N, M, V = map(int, input().split())

# 인접행렬
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1


# DFS
def dfs(v):
    visited[v] = True
    dfs_nodes.append(str(v)) # 저장
    for i in range(1, N+1):
        if not visited[i] and matrix[v][i] == 1:
            dfs(i)

# BFS
def bfs(v):
    q = deque([v])
    visited[v] = True
    # 큐가 빌 때까지 반복
    while q:
        v = q.popleft()
        bfs_nodes.append(str(v)) # 저장
        for i in range(1, N+1):
            if not visited[i] and matrix[v][i] == 1:
                q.append(i)
                visited[i] = True


# 방문한 노드를 저장하는 1차원 리스트
visited = [False for _ in range(N+1)]
dfs_nodes = []
dfs(V)
print(" ".join(dfs_nodes))

# 방문한 노드를 저장하는 1차원 리스트
visited = [False for _ in range(N+1)]
bfs_nodes = []
bfs(V)
print(" ".join(bfs_nodes))
