from collections import deque

def solution(maps):
    n=len(maps) ; m=len(maps[0])
    visited=[[0]*m for _ in range(n)]
    
    def bfs(maps,x,y):
        dx=[0,0,1,-1] ; dy=[1,-1,0,0]
        queue=deque([(x,y)])
        visited[x][y]=True
        distance={(x,y):1}
        
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i] ; ny=y+dy[i]
                if (nx,ny)==(n-1,m-1):
                    return distance[(x,y)]+1
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=True
                    distance[(nx,ny)]=distance[(x,y)]+1
                    queue.append((nx,ny))
        return -1
    
    return bfs(maps,0,0)
    
