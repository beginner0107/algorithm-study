import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int, input().split())

#1 익은토마토, 0 안 익음, -1 또마토 없음
graph = []
queue = deque([])

for i in range(h):
    temp=[]
    for j in range(n):
        temp2 = list(map(int, input().split()))
        for k in range(len(temp2)) :
            #익은 토마토이면 queue에 위치 집어넣음
            if temp2[k]==1: 
                queue.append((i,j,k))
        temp.append(temp2)
    graph.append(temp)

dx=[1,-1,0,0,0,0] ; dy=[0,0,1,-1,0,0] ; dz=[0,0,0,0,1,-1]

while queue:    
    x,y,z = queue.popleft()
    for i,j,k in zip(dx,dy,dz):
        nx,ny,nz = x+i, y+j, z+k
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
            queue.append((nx,ny,nz))
            graph[nx][ny][nz] = graph[x][y][z] + 1


flatten =  sum(sum(graph,[]),[])

if 0 in flatten:
    print(-1)
else:
    print(max(flatten)-1)
