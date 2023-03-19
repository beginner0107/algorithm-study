import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomatoLayer = []
tomatoBox = []
for _ in range(H):
    for _ in range(N):
        tomatoLayer.append(list(map(int, sys.stdin.readline().split())))
    tomatoBox.append(tomatoLayer)
    tomatoLayer = []

queue = deque()
xx = [1, -1, 0, 0, 0, 0]
yy = [0, 0, 1, -1, 0, 0]
zz = [0, 0, 0, 0, 1, -1]

notRipen = 0
ripen = []
# 전체를 확인하면서, 익은 토마토는 위치 저장, 안 익은 토마토는 개수 카운트
for layer in range(H):
    for row in range(N):
        for col in range(M):
            if tomatoBox[layer][row][col] == 1:
                ripen.append([layer, row, col])
            elif tomatoBox[layer][row][col] == 0:
                notRipen += 1

# 안 익은 토마토가 없으면 0 출력
if notRipen == 0:
    print(0)
# 안 익은 토마토가 있으면 bfs
else:
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    day = 0
    # 익은 토마토 위치 모두 추가, visited=1
    for i in range(len(ripen)):
        queue.append([ripen[i][0], ripen[i][1], ripen[i][2], day])
        visited[ripen[i][0]][ripen[i][1]][ripen[i][2]] = 1

    while queue:
        layer, row, col, day = deque.popleft(queue)

        for i in range(6):
            newLayer = layer + zz[i]
            newRow = row + xx[i]
            newCol = col + yy[i]
            if 0 <= newLayer < H and 0 <= newRow < N and 0 <= newCol < M:
                # 새로운 위치가 안 익은 토마토일 경우, push, visitied=1, day+1, 익은 토마토로
                if tomatoBox[newLayer][newRow][newCol] == 0 and not visited[newLayer][newRow][newCol]:
                    queue.append([newLayer, newRow, newCol, day + 1])
                    visited[newLayer][newRow][newCol] = 1
                    tomatoBox[newLayer][newRow][newCol] = 1

    flag = 0
    for layer in range(H):
        for row in range(N):
            for col in range(M):
                # 안 익은 토마토가 하나라도 있으면, -1 출력 후 break
                if tomatoBox[layer][row][col] == 0:
                    flag = 1
                    print(-1)
                    break
            if flag == 1:
                break
        if flag == 1:
            break
    # 안 익은 토마토가 없으면, day 출력
    if flag == 0:
        print(day)