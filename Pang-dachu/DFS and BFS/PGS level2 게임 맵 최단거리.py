from collections import deque

def bfs(maps, x,y ) :
    q = deque()
    q.append( (x,y) )
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q :
        x,y = q.popleft()
        
        for i in range(0,4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # maps 를 벗어나지 않는 거리에서 수행
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) : 
                
                # 0인 경우 벽, continue 
                if maps[nx][ny] == 0 :
                    continue
                
                # 1인 경우 길, 
                elif maps[nx][ny] == 1 :
                    # 경로에 1씩 증가 
                    maps[nx][ny] = maps[x][y] + 1
                    q.append( (nx, ny) )
    
    return -1 if maps[-1][-1] == 1 else maps[-1][-1]

def solution(maps):
    # 일반적으로 그래프가 크지 않은경우 BFS가 좋은편 
    # 미로의 최단거리는 BFS가 좋은 것으로 알고 있음
    
    # 시작은 (0,0) 
    return bfs(maps, 0,0)