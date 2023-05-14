n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)] ; dp[0][0]=graph[0][0]

for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        elif i==0 and j>0:
            dp[i][j] = dp[i][j-1] + graph[i][j]
        elif i>0 and j==0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + graph[i][j]


print(max(map(max,dp)))



