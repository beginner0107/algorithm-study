# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택
# 삼각형의 크기는 1 이상 500 이하, 모두 정수이며, 범위는 0 이상 9999 이하

# 바로 아래에 있는 것 / 아래에서 하나 오른쪽에 있는 것 선택 가능
# 하나씩 아래로 내려가면서 확인

import sys
input = sys.stdin.readline

n = int(input())    # 정수 삼각형의 크기
triangle = [list(map(int, input().split())) for _ in range(n)]    # 정수 삼각형의 정보
dp = []    # 해당 위치의 최대 합
for i in range(1, n + 1):
    dp.append([0] * i)
dp[0] = triangle[0]    # 시작 위치 초기화
    
# 순차적으로 탐색
for r in range(1, n):    # (2 ~ n) 탐색
    for c in range(r + 1):
        if c == 0:    # 왼쪽 변의 값이라면,
            dp[r][c] = triangle[r][c] + dp[r - 1][c]    # 바로 위의 값
        elif c == r:    # 오른쪽 변의 값이라면,
            dp[r][c] = triangle[r][c] + dp[r - 1][c - 1]    # 바로 위의 값
        else:     # 중앙의 값이라면,
            dp[r][c] = triangle[r][c] + max(dp[r - 1][c - 1:c + 1])    # (r - 1)의 (c - 1, c) 탐색
            
print(max(dp[n - 1]))
            