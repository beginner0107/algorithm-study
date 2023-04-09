import sys
n = int(sys.stdin.readline())

day = [0] * (n+1)       # 일 수
income = [0] * (n+1)    # 벌 수 있는 금액

# 값 입력
for i in range(1, n+1) :
    day[i], income[i] = map(int, sys.stdin.readline().split())

# dp 배열
dp = [0] *(n+2)

for i in range(n, -1, -1) :
    if i+day[i] > n+1 :     # 일을 못할 경우 보상을 변화시키지 않음
        dp[i] = dp[i+1]
    else :                  # 일을 할지 안할지 더 큰 보상을 보고 선택
        dp[i] = max(dp[i+1], dp[i+day[i]] + income[i]) 

print(dp[0])
