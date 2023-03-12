from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    n = len(maps)
    m = len(maps[0])
    
    # 방문 리스트
    visited = [[-1]*m for _ in range(n)]

    q = deque()
    
    q.append((0, 0))
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            
            # 범위 벗어나면 continue
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
                
            # 벽이 없고, 방문하지 않았으면
            if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return visited[n-1][m-1]