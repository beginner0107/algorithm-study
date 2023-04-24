import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

cnt = 1
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs():
    global cnt
    q = set([(0, 0, board[0][0])])
    
    while q:
        x, y, z = q.pop()
        
        # 말이 지나갈 수 있는 최대 칸
        cnt = max(cnt, len(z))
        
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            # 지난 알파벳이 아닌 경우, 추가 & dfs 진행
            if board[nx][ny] not in z:
                q.add((nx, ny, board[nx][ny] + z))
bfs()
print(cnt)