import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []

#1. graph 정보 입력
for _ in range(n):
    graph.append(list(input()))
    
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = [[0,0]]

graph[0][0]=1

while queue:
    x, y = queue[0][0], queue[0][1]
    
    del queue[0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx<n and ny<m:
            if graph[nx][ny] == "1":
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
                
print(graph[n-1][m-1])
