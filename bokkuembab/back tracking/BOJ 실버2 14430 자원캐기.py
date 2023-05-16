# 왼쪽 위 (1, 1)부터 오른쪽 아래 (N, M)까지 자원을 탐색
# 한 번에 오른쪽 또는 아래쪽으로 한 칸 이동
# 자신이 위치한 (x, y)에 자원이 있는 경우에만 해당 자원을 채취
# WOOK이 탐색할 수 있는 자원의 최대 숫자
# 자원: 1, 빈 땅: 0

# (r, c)까지의 자원의 최대 숫자들을 구해서 저장하면 됨 -> dp

import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 탐사할 영역의 행, 열의 크기
explore = [list(map(int, input().split())) for _ in range(n)]    # 탐사할 영역의 정보
dp = [[0] * m for _ in range(n)]    # 해당 영역까지의 최대 탐색 자원 수
dp[0][0] = explore[0][0]    # 시작 위치 초기화

# 순차적으로 탐색 시작
for r in range(n):
    for c in range(m):
        if r == 0 and c == 0:    # 시작 위치이면, 넘어가기
            continue
        elif r == 0 and c > 0:    # 첫 줄이면, 이전 칼럼의 값과 비교
            dp[r][c] = explore[r][c] + dp[r][c - 1]
        elif r > 0 and c == 0:    # 첫 열이라면, 이전 행의 값과 비교
            dp[r][c] = explore[r][c] + dp[r - 1][c]
        else:    # 첫 행, 첫 열이 아니라면, 오른쪽/아래쪽 방향 이동 중 큰 값 비교
            dp[r][c] = explore[r][c] + max(dp[r][c - 1], dp[r - 1][c])
            
print(dp[n - 1][m - 1])