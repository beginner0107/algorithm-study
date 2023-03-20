from collections import deque
import sys
#input = sys.stdin.readline

m, n, h = map(int,input().split())
farm = []
q = deque([])
moves = [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
day = 0

# 익은 토마토가 있는 위치 입력
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k]==1:
                q.append([i,j,k])
    farm.append(tmp)

while(q):
    x, y, z = q.popleft()    
    for dx, dy, dz in moves:
        nx, ny, nz = x+dx, y+dy, z+dz
        if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
            continue
        if farm[nx][ny][nz] == 0:
            q.append([nx, ny, nz])
            farm[nx][ny][nz] = farm[x][y][z] + 1

for i in farm:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)
