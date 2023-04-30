import sys

r, c = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0] ; dy = [0, 0, -1, 1]

ans = 1

def bfs(x, y):
    global ans
    alphabet = set([(x, y, maps[x][y])])
    while alphabet:
        x, y, new_ans = alphabet.pop()
        for i, j in zip(dx, dy):
            nx = x + i ; ny = y + j
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] not in new_ans:
                alphabet.add((nx,ny,new_ans + maps[nx][ny]))
                ans = max(ans, len(new_ans)+1)
bfs(0, 0)
print(ans)
