# 0-1 knapsack
def knapsack(W, wt, val, n):
    # 2차원 리스트 K 초기화
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            # 담을 것이 없으면 담지 않음
            if i == 0 or w == 0:
                K[i][w] = 0
            # i 번째 물건을 담을 수 있을 때 담을 때와 담지 않을 때 가치 비교
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            # 현재 물건의 무게가 남은 용량보다 클 때, 최대 가치를 가져옴
            else:
                K[i][w] = K[i - 1][w]
    
    return K[n][W]

wt = []
val = []

n, m = map(int, input().split())

for i in range(n) :
    p = list(map(int, input().split()))
    wt.append(p[0])
    val.append(p[1])

print(knapsack(m, wt, val, n))
    
