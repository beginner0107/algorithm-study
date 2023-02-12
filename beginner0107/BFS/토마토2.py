import sys
from collections import deque


# 상자의 크기를 나타내는 두 정수

# 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# 1 or 0인 경우에만 -1은 상관 없음

def bfs():
    # queue 사용
    q = deque()
    # 익은 토마토의 위치를 체크해줄 visited 배열
    v = [[[0] * M for _ in range(N)] for _ in range(H)]
    # 익지 않은 토마토의 개수를 저장할 cnt 변수
    cnt = 0
    for h in range(H):  # 전체순회하며 처리
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:   # 익은 토마토
                    q.append((h, i, j)) # 위치를 queue에 저장
                    v[h][i][j] = 1      # 익은 토마토에는 1의 표시
                elif arr[h][i][j] == 0: # 익지 않은 토마토의 개수
                    cnt += 1

    while q: # 큐 안에는 익은 토마토의 위치들이 들어가 있게 된다.
        ch, ci, cj = q.popleft()

        # 6방향으로 탐색을 시작
        for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nh, ni, nj = ch + dh, ci + di, cj + dj # 계산된 좌표를 구하고
            # 범위 내에 있는지 확인, 익지 않은 토마토인지 확인, 처음 방문한 경우에만 if문 실행
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0:
                q.append((nh, ni, nj)) # 큐에다 좌표를 넣어주고
                v[nh][ni][nj] = v[ch][ci][cj] + 1 # 방문을 했기에 이전 좌표에 1을 더해준다.
                cnt -= 1 # 안 익은 토마토의 개수 1을 감소
    if cnt == 0:  # 모든 토마토 익었음
        return v[ch][ci][cj] - 1 # 마지막 큐에 담긴 좌표의 값에 -1을 해준 값이 답
    else: # cnt가 0보다 크다 -> 안 익은 토마토가 남아있다는 뜻
        return -1 # -1을 리턴한다

# 상자의 크기를 나타내는 두 정수 M, N
M, N, H = map(int, sys.stdin.readline().split())

arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

ans = bfs()

print(ans)
