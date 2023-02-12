import sys
from collections import deque

t = int(sys.stdin.readline())  # 테스트 케이스의 개수

# 나이트의 이동 좌표 계산을 위한 dx, dy
dx = [-1, 1, 2, 2, 1, -1, -2, -2] 
dy = [2, 2, 1, -1, -2, -2, -1, 1]


def bfs():
    q = deque()
    q.append((x, y)) 
    # 방문한 좌표를 저장할 2차원 배열
    visited = [[0 for _ in range(l)] for _ in range(l)] 
    while q:
        ax, ay = q.popleft()
        # 이동하려고 하는 최종 목적지에 도착한 경우
        if ax == tx and ay == ty:
            return visited[ax][ay]
        else:
            # 나이트를 이동 시킨다
            for i in range(0, 8):
                nx = ax + dx[i]
                ny = ay + dy[i]
                # 체스판의 범위 안에, 혹은 처음 방문했을 경우
                if l > nx >= 0 and 0 <= ny < l and 0 == visited[nx][ny]:
                    visited[nx][ny] = visited[ax][ay] + 1 # 이전 방문횟수 + 1
                    q.append((nx, ny))


while t > 0:
    l = int(sys.stdin.readline())  # 체스판의 한 변의 길이
    x, y = map(int, sys.stdin.readline().split())  # 현재 위치
    tx, ty = map(int, sys.stdin.readline().split())  # 이동하려는 칸
    cnt = bfs()
    print(cnt)
    t -= 1