# 정수 1은 익은 토마토
# 정수 0 은 익지 않은 토마토
# 정수 -1은 토마토가 들어있지 않은 칸

from collections import deque

def bfs():
    while dq:
        z, x, y = dq.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            # box 범위 밖이면 continue
            if 0 > nx or 0 > ny or 0 > nz or nx >= n or ny >= m or nz >= h:
                continue
            
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                dq.append([nz, nx, ny])


m, n, h = map(int, input().split())

# 6방향에 대한 dx, dy, dz
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

# box 입력
box = [[list(map(int, input().split())) for i in range(n)] for dep in range(h)]

dq = deque()

# 익은 토마토 좌표만 dq에 넣어줌
for k in range(h):
    for x in range(n):
        for y in range(m):
            if box[k][x][y] == 1:
                dq.append([k,x,y])  
                
bfs()

answer = -1

for k in range(h):
    for x in range(n):
        for y in range(m):
            # 안 익은 토마토만 가득 차 있을 경우
            if box[k][x][y] == 0:
                print(-1)
                exit(0)
            else:
                answer = max(answer, box[k][x][y])
print(answer - 1)