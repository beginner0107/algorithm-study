# https://www.acmicpc.net/problem/14430

"""
문제
인류의 차세대 인공지능 자원 캐기 로봇인 WOOK은 인간 대신 자원을 캐는 로봇이다. WOOK은 언제나 제한된 범위 내에서 자원을 탐색하며, 왼쪽 위 (1, 1)부터 오른쪽 아래 (N, M)까지 자원을 탐색한다. WOOK은 한 번에 오른쪽 또는 아래쪽으로 한 칸 이동할 수 있으며, 그 외의 방향으로 움직이는 것은 불가능하다. WOOK은 자신이 위치한 (x, y)에 자원이 있는 경우에만 해당 자원을 채취할 수 있다. WOOK이 탐사할 영역에 대한 정보가 주어질 때, WOOK이 탐색할 수 있는 자원의 최대 숫자를 구해라!

입력
첫째 줄에 WOOK이 탐사할 영역의 세로길이 N(1≤N≤300)과 가로길이 M(1≤M≤300)이 주어진다. 그 다음 N행 M열에 걸쳐 탐사영역에 대한 정보가 주어진다. 숫자는 공백으로 구분된다. (자원은 1, 빈 땅은 0으로 표시된다)

출력
WOOK이 수집할 수 있는 최대 광석의 개수를 출력하라.

예제 입력
5 4
0 1 0 0
0 0 1 0
1 1 0 0
1 0 1 0
1 1 0 0

예제 출력
4
"""

"""
from collections import deque

n, m = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(n)]

# 하, 우 이동
mx = [0, 1]
my = [1, 0]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(2):
        nx = x + mx[i]
        ny = y + my[i]

        if 0 <= nx < n and 0 <= ny < m:
            q.append((nx, ny))

            if space[nx][ny] == 1:
                space[nx][ny] = space[x][y] + 1

print(max(map(max, space)))
"""
# bfs는 메모리 낭비 발생 -> dp 로 진행

import sys; input=sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)] # 0 으로 초기화
space = [list(map(int, input().split())) for _ in range(n)] # 입력

for i in range(n):
    for j in range(m):
        # 현재 값이 1이면 1로 초기화
        if space[i][j] == 1:
            dp[i][j] = 1
        # 왼쪽, 위쪽 중 큰 값 + 현재 값
        if i > 0 and j > 0:
            dp[i][j] = space[i][j] + max(dp[i - 1][j], dp[i][j - 1])
        # 왼쪽이나 위쪽이 없을 경우
        elif i > 0:
            dp[i][j] = space[i][j] + dp[i - 1][j]
        elif j > 0:
            dp[i][j] = space[i][j] + dp[i][j - 1]

print(dp[n - 1][m - 1])

