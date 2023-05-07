def solution(n, money):
    dp = [0] * (n+1)  # dp[i]: i원을 거슬러주는 방법의 수

    dp[0] = 1  # 0원을 만드는 경우 1개

    for coin in money:
        for i in range(coin, n+1):
            dp[i] = dp[i] + dp[i-coin]
    return dp[n]
