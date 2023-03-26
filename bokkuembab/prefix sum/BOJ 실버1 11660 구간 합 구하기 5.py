import sys
input = sys.stdin.readline

# 값 입력 받기
n, m = map(int, input().split())    # n: 표의 한 변의 길이, m: 합을 구해야 하는 횟수
table = []    # 테이블의 정보
for _ in range(n):
    table.append(list(map(int, input().split())))

# 누적합 구하기
pref_sum = [[0] * (n + 1) for _ in range(n + 1)]    # 누적합 테이블 초기화
for r in range(1, n + 1):
    for i in range(1, n + 1):
        pref_sum[r][i] = table[r - 1][i - 1] + pref_sum[r - 1][i] + pref_sum[r][i - 1] - pref_sum[r - 1][i - 1]

# 구간 입력 받으며, 구간합 구하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(pref_sum[x2][y2] - pref_sum[x1 - 1][y2] - pref_sum[x2][y1 - 1] + pref_sum[x1 - 1][y1 - 1])