N, K = map(int, input().split())

# dp 테이블 초기화 
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, K+1):
    w, t = map(int, input().split())
    for j in range(1, N+1):
        # 현재 과목을 선택하지 않는 경우 
        dp[i][j] = dp[i-1][j]
        # 현재 과목을 선택하는 경우 
        if j >= t:
            dp[i][j] = max(dp[i][j], dp[i-1][j-t] + w)

print(dp[K][N])
