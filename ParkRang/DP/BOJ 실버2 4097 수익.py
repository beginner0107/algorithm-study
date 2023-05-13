import sys
while True:
    n = int(sys.stdin.readline())  # 수열의 길이 입력
    if n == 0:
        break

    seq= []
    for _ in range(n):
        seq.append(int(sys.stdin.readline()))  # 수열의 원소 입력

    dp = [0] * n
    dp[0] = seq[0]
    max_sum = dp[0]

    for i in range(1, n):
        dp[i] = max(seq[i], dp[i-1] + seq[i])
        max_sum = max(max_sum, dp[i])

    print(max_sum)
