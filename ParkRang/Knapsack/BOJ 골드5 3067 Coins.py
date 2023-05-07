T = int(input())  # 테스트 케이스

for _ in range(T):
    N = int(input())  # 동전 종류의 개수
    coins = list(map(int, input().split()))  # 동전의 가치
    M = int(input())  # 만들 금액

    dp = [0] * (M+1)  # i원을 만들 수 있는 경우의 수

    dp[0] = 1  # 0원을 만들기 위한 경우 1가지 (아무 동전도 사용하지 않음)

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] = dp[i] + dp[i-coin]

    print(dp[M])
