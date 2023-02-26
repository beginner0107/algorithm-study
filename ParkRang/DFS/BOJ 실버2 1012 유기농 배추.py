# 백준 1012 유기농 배추 실버2
# 백준 에러 제거
import sys
sys.setrecursionlimit(10000)

# 상하좌우 배열
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# dfs 함수
def dfs(x, y) :
    # 종료 조건
    if x<0 or x>=N or y<0 or y>=M :
        return False
    # 수행 동작
    if field[x][y] == 1:
        field[x][y] = 0
        for i in range(4) :
            dfs(x+dx[i], y+dy[i])
        return True
    return False

# 횟수
n = int(input())

# 땅 입력
while n>0 :
    answer = 0 # 제출할 값
    
    size = []
    M,N,K = map(int, input().split())

    field = []
    MN = [0] * M
    for i in range(N) :
        field.append(MN.copy())
    

# 배추 입력
    for i in range(K) :
        cabbageY, cabbageX = map(int, input().split())
        field[cabbageX][cabbageY] = 1

# 배열을 돌며 dfs 호출
    for i in range(N) :
        for j in range(M) :
            if dfs(i, j) :
                answer = answer + 1
    
    print(answer)

# 한개의 테스트 종료
    n = n-1


