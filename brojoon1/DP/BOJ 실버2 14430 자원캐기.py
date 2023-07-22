n, m = map(int, input().split())
graph = []
dp = [[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))
    
dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        # (0,0) 일땐 continue
        if i == 0 and j == 0:
            continue
        # 벽에 붙어서 x축 방향으로 갈 때
        elif i > 0 and j == 0:
            dp[i][j] = dp[i-1][j]
        # 벽에 붙어서 y축 방향으로 갈 때
        elif i == 0 and j > 0:
            dp[i][j] = dp[i][j-1]
        # 아닐 땐 둘 중 큰 값
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        if graph[i][j] == 1:
            dp[i][j] += 1

print(dp[n-1][m-1])