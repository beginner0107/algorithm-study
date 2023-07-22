import sys
input = sys.stdin.readline

N, M = map(int, input().split())
resource = [list(map(int, input().split())) for _ in range(N)]

for i in range(N) :
    for j in range(M) : 
        if i == j == 0 :
            continue
        elif i == 0 :
            resource[i][j] += resource[i][j-1]
        elif j == 0 :
            resource[i][j] += resource[i-1][j]
        else:
            resource[i][j] += max(resource[i][j-1], resource[i-1][j])
print(resource[-1][-1]) 