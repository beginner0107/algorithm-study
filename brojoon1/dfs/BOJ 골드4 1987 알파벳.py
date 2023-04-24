import sys

answer = 0

def dfs(y, x, before):
    global answer
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 다음 방문할 곳이 들리지 않은 곳 이면
        if 0 <= nx < C  and 0 <= ny < R and board[ny][nx] not in before:
            dfs(ny, nx, before+board[ny][nx])
    
    answer = max(answer, len(before))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, sys.stdin.readline().split())

board = []
for _ in range(R):
    board.append(input())
    
dfs(0, 0, board[0][0])

print(answer)