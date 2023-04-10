# 0-1 knapsack
def knapsack(L, time, val, n) :
    # 2차원 리스트 K 초기화
    K = [[0 for x in range(L+1)] for x in range(n+1)]

    for i in range(n+1) :
        for l in range(L+1) :
            if i==0 or l==0 :
                K[i][l] = 0
            # i 단원을 공부했을때와 공부하지 않았을 때 가치 비교
            elif time[i-1] <= l :
                K[i][l] = max(val[i-1] + K[i-1][l - time[i-1]], K[i-1][l])
            # 현재 단원의 시간이 남은 시간보다 클 때 최대의 가치를 가져옴
            else :
                K[i][l] = K[i-1][l]

    return K[n][L]

time = []
val = []

n, m = map(int, input().split())

for _ in range(n) :
    p = list(map(int, input().split()))
    time.append(p[0])
    val.append(p[1])

print(knapsack(m, time, val, n))
