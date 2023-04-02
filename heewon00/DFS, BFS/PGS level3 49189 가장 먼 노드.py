from collections import deque

def solution(n, edge):
    distance = [0]*(n+1)
    
    graph = [[] for _ in range(n+1)]
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    def bfs(start):
        queue=deque([start])
        visited=[0]*(n+1) ; visited[start]=1
        
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    distance[i] = distance[v] + 1
    bfs(1)
    return distance.count(max(distance))
                
