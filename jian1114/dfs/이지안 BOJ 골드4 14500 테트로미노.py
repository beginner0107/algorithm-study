import sys
input = sys.stdin.readline
# 입력 받기
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 방문여부 리스트
visited = [[False for _ in range(M)] for _ in range(N)]

# 상하좌우 
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# dfs 
def dfs(x, y, total, size):
    global ans
    
    ## 1. 4번째 블록인 경우, return
    if size == 4:
        # 이전까지의 최댓값, 현재 dfs 진행한 값 중 최댓값 
        ans = max(ans, total)    
        return 
    
    # 상 하 좌 우
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        
        # 보드를 벗어나지 않고, 방문하지 않은 경우
        if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
            
            ## 2. 2번째 블록인 경우(ㅗ모양 고려)
            if size == 2:
                visited[nx][ny] = True
                dfs(x, y, total+board[nx][ny], size+1)
                visited[nx][ny] = False
            
            ## 3. 1,3번째 블록인 경우,
            visited[nx][ny] = True
            dfs(nx, ny, total+board[nx][ny], size+1)
            visited[nx][ny] = False

            
# 결과값
ans = 0
for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, board[x][y], 1)
        visited[x][y] = False
print(ans)