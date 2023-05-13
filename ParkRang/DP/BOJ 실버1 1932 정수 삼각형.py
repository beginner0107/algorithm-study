import sys
n = int(sys.stdin.readline())

# 삼각형 배열
tri = []

# 삼각형 배열 입력
for i in range(n) :
    tri.append(list(map(int, sys.stdin.readline().split())))

# 삼각형 배열 값에 최대가 될 수 있도록 값을 더해줌
# 이후에 가장 높은 값을 선택함
for i in range(1, n) :
    for j in range(len(tri[i])) :
        if j== 0 :
            tri[i][0] = tri[i][0] + tri[i-1][0]
        elif j == len(tri[i])-1 :
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else :
            tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))
        
