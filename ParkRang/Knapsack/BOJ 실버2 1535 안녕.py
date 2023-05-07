N = int(input())  # 인사할 사람의 수
L = list(map(int, input().split()))  # 각 사람의 체력
J = list(map(int, input().split()))  # 각 사람마다 얻는 기쁨

dp = [[0] * 101 for _ in range(N+1)]  # dp[i][j]: i번째 사람, j만큼의 체력을 사용, 얻을 수 있는 최대 기쁨

for i in range(1, N+1):
    for j in range(1, 101):
        if j >= L[i-1]:  # j만큼의 체력을 사용 가능한 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i-1]] + J[i-1])
        else:  # j만큼의 체력을 사용 불가능한 경우
            dp[i][j] = dp[i-1][j]

print(dp[N][99])  # 체력 100-1에서 최대 기쁨 출력
