# n: 정점 수, m: 간선 수, v: 탐색 시작 번호

from collections import deque
import sys
input = sys.stdin.readline

# DFS 함수
def dfs(graph, v, visited):
    
    # 1. 방문했음을 표시
    visited[v] = True
    
    # 2. 출력
    print(v, end=' ')
    
    # 3. 연결된 노드들 재귀적으로 방문하기
    for i in graph[v]:
        if not visited[i]:    # 4. 방문한 노드가 아니라면, 방문
            dfs(graph, i, visited)

# BFS 함수
def bfs(graph, v, visited):
    
    # 1. deque 선언
    queue = deque([v])
    
    # 2. 방문했음을 표시
    visited[v] = True
    
    # 3. queue가 빌 때까지 반복
    while queue:
        
        # 4. queue에서 하나 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        
        # 5. 연결된 노드들 방문하기
        for i in graph[v]:
            if not visited[i]:    # 방문하지 않았다면, queue에 
                queue.append(i)
                visited[i] = True    # 방문처리

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선들 입력 받기
for _ in range(m):
    n1, n2 = map(int, input().split())
    
    graph[n1].append(n2)
    graph[n2].append(n1)

for row in range(n + 1):
    graph[row].sort()
    

# DFS 출력
visited = [False] * (n + 1)    # 방문 정보 리스트 초기화
dfs(graph, v, visited)
print()

# BFS 출력
visited = [False] * (n + 1)    # 방문 정보 리스트 초기화
bfs(graph, v, visited)