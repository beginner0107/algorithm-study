from collections import deque
M, N, H = map(int, input().split())

# 토마토와 큐와 날짜
A = []
q = deque()
day = 0


# 좌표 계산 배열
dx = [-1,0,0,1,0,0]
dy = [0,-1,0,0,1,0]
dz = [0,0,-1,0,0,1]
                
        
# 토마토 배열에 추가
for i in range(N*H) :
    A.append(list(map(int, input().split())))

# 1인 토마토 큐에 추가  
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if A[i*N + j][k] == 1:
                q.append([i,j,k])

# 큐 값을 가져와서 확인
while q:
    day = day + 1
    for i in range(len(q)) :
        x,y,z = q.popleft()
        for j in range(6) :
            X, Y, Z = x + dx[j], y + dy[j], z + dz[j]
            if 0 <= X < H and 0 <= Y < N and 0 <= Z < M and A[X*N + Y][Z] == 0:
                A[X*N + Y][Z] = 1
                q.append([X,Y,Z])

# 토마토 상태 확인
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if A[i*N + j][k] == 0:
                print(-1)
                exit()

print(day-1)
