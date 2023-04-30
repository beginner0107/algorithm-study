# pypy로 성공, python3 실패
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 제한 해제

r, c = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(r)]
visited = [False] * 26 # 알파벳의 개수(26)만큼 visited 배열 생성

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 상하좌우 이동

def dfs(x, y, cnt):
    # 수행동작
    global answer
    answer = max(answer, cnt) # 최대 이동 횟수 갱신
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # ord() : 문자의 유니코드 코드 포인트 값 반환
        if 0 <= nx < r and 0 <= ny < c and not visited[ord(board[nx][ny]) - ord('A')]:
            visited[ord(board[nx][ny]) - ord('A')] = True # 해당 알파벳 방문 체크
            dfs(nx, ny, cnt + 1)
            visited[ord(board[nx][ny]) - ord('A')] = False # 해당 알파벳 방문 체크 해제

answer = 1
visited[ord(board[0][0]) - ord('A')] = True # 시작 위치의 알파벳 방문 체크
dfs(0, 0, answer)
print(answer)
