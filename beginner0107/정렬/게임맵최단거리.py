from collections import deque
def solution(maps):
    cnt = dfs(maps)
    if cnt == 0: return -1
    return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(maps):
    visited = [[0 for j in range(len(maps[0]))] for i in range(len(maps))]
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 1 or visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((int(nx), int(ny)))
    return visited[len(maps) - 1][len(maps[0]) - 1]