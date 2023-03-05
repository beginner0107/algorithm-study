# 백준 2210 숫자판 실버2
# 숫자판을 입력받을 배열
numbers = []

# 상하좌우로 움직일 수치
dx = [-1,0,1,0]
dy = [0, -1, 0, 1]

# 값을 저장할 리스트
six = []

# dfs 함수
def dfs(x, y, num) : # x좌표, y좌표, 커질 숫자들
    # 1. 종료 조건
    if x<0 or x>=5 or y<0 or y>=5 or len(num)>=7:
        return False
    if len(num) == 6 :
        if num not in six :
            six.append(num)
    # 2. 수행 동작
    else :
        num = num + numbers[x][y]
        for i in range(4) :
            dfs(x+dx[i], y+dy[i], num)

# 5 x 5 배열 입력
for i in range(5) :
    numbers.append(list(map(str, input().split())))

# 5 x 5 dfs 수행
for i in range(5) :
    for j in range(5) :
        dfs(i, j, '')

# 6자리 수의 갯수 합산
print(len(six))
