from collections import deque
import sys
#input = sys.stdin.readline

m, n = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
q = deque([])
day = 0

# 익은 토마토가 있는 위치 입력
for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이동한 위치가 안 익은 토마토인 경우, 계속 +1을 해주며 갱신
            # 즉, 1부터 시작하여 0에 접근할 수 있을 때까지 날짜 갱신
            if farm[nx][ny] == 0:
                farm[nx][ny] = farm[x][y] + 1
                q.append([nx, ny])

# bfs()를 실행하면, 영향을 받을 수 있는 모든 토마토는 1 이상의 값을 가지게 됨
bfs()

# 행 별로 접근하며, 만약 안 익은 토마토가 있는 경우, -1 출력 & 종료
# 만약 0이 없다면 그 행에서 가장 큰 값을 ans에 저장
for i in farm:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day - 1)