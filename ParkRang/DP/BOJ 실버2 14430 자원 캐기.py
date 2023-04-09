import sys

n, m = map(int, sys.stdin.readline().split())

# 자원을 저장할 배열
resource = []
ans = 0

# 자원 입력
for i in range(n) :
    resource.append(list(map(int, sys.stdin.readline().split())))

# n x m에서 아래와 오른쪽으로만 갈 수 있으므로
# 위에서 온 값과 왼쪽에서 온 값중 높은 값에 현재 값을 더한 값을 자원으로 저장
for i in range(n) :
    for j in range(m) : 
        if i > 0 and j > 0:
            resource[i][j] = max(resource[i-1][j], resource[i][j-1]) + resource[i][j]
        elif i > 0 :
            resource[i][j] = resource[i-1][j] + resource[i][j]
        elif j > 0 :
            resource[i][j] = resource[i][j-1] + resource[i][j]
        if resource[i][j] > ans :
            ans = resource[i][j]

print(ans) 
