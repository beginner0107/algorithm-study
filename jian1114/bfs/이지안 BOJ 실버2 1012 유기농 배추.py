from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]     
dy = [0, 0, 1, -1]    

def bfs(x, y):
    q = deque([[x,y]])
    graph[x][y] = 0 

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = -1
                    q.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [ [0] * M for _ in range(N)]  
  
    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1     

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:   # 해당 위치에 배추가 있다면, 
                bfs(i, j)          # bfs 진행 
                answer += 1    
    print(answer)