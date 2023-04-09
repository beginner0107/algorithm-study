
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for i in range(n+1)]

dp[1] = [0, 1,1,1,1,1,1,1,1,1]
for i in range(2, n+1):
    for j in range(10):
        if j == 0: #뒤에 1만 올수있음
            dp[i][j] = dp[i-1][1]
        elif j == 9: #뒤에 8만 올 수 있음
            dp[i][j] = dp[i-1][8]
            
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
