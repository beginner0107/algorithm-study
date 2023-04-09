from collections import deque

def solution(n, results):
    answer=0
    
    win = [ [] for _ in range(n+1) ]
    lose = [ [] for _ in range(n+1) ]
    
    for i, j in results:
        win[i].append(j)
        lose[j].append(i)
        
    def bfs(start, graph, visited):
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i) ; visited[i] = 1 
        return visited

    for i in range(1, n+1):
        visited = [0]*(n+1)
        bfs(i, win, visited)
        bfs(i, lose, visited)
        if visited.count(1)==n-1: #자신 제외
            answer+=1

    return answer
