from collections import deque
import sys


def bfs():
    # queue 사용
    q = deque()
    # 익지 않은 토마토의 개수를 저장할 cnt 변수
    cnt = 0
    # 익은 토마토의 위치를 체크해줄 visited 배열
    visited = [[0] * N for _ in range(M)]
    for m in range(M):
        for n in range(N):
            if arr[m][n] == 1:    # 익은 토마토라면
                q.append((m, n))  # 위치를 queue에 저장
                visited[m][n] = 1 # 익은 토마토에는 1의 표시
            elif arr[m][n] == 0:  # 익지 않은 토마토의 개수
                cnt += 1

    while q: # 큐 안에는 익은 토마토의 위치들이 들어가 있게 된다.
        cm, cn = q.popleft() 
        for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)): # 4방향으로 탐색을 시작
            rm, rn = i + cm, j + cn # 계산된 좌표를 구하고
            # 범위 내에 있는지 확인 and 익지 않은 토마토인지 확인
            if 0 <= rm < M and 0 <= rn < N and arr[rm][rn] == 0:
                # 처음 방문한 경우에만 if문 실행
                if visited[rm][rn] == 0:
                    q.append((rm, rn)) # 큐에다 좌표를 넣어주고
                    # 방문을 했기에 이전 좌표에 1을 더해준다.
                    visited[rm][rn] = visited[cm][cn] + 1 
                    cnt -= 1 # 안 익은 토마토의 개수 1을 감소

    if cnt == 0: # 모두 익은 토마토가 되었다는 의미
        return visited[cm][cn] - 1 # 마지막 큐에 담긴 좌표의 값에 -1을 해준 값이 답
    else: # cnt가 0보다 크다 -> 안 익은 토마토가 남아있다는 뜻
        return -1 # -1을 리턴한다

# 상자의 크기를 나타내는 두 정수 M, N
N, M = map(int, sys.stdin.readline().split())
# 2차원 배열을 생성하기 위해 arr 생성
arr = list()
# 2차원 배열 입력 받기
for i in range(M):
    arr.append(list(map(int, sys.stdin.readline().split())))
print(bfs()) # 토마토가 모두 익을 때까지의 최소 날짜 출력