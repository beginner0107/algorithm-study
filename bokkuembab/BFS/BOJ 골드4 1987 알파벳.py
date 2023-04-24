import sys
from collections import deque
input = sys.stdin.readline   

row, col = map(int, input().split())    # 세로, 가로의 길이
board = [list(map(str, input().rstrip())) for _ in range(row)]    # 보드의 정보


# (0, 0) 위치부터 시작
moves = 1    # 움직인 횟수
q = set([(0, 0, board[0][0])])    # (row 위치, col 위치, 지금까지 지나온 알파벳: 알파벳이 위치 방문 여부도 확인해줌)

while q:
    r, c, chars = q.pop()
    
    # 최대 이동 수 초기화
    moves = max(moves, len(chars))
    
     # 이동 가능한 경우의 수 (상하좌우)
    mover = [-1, 1, 0, 0]
    movec = [0, 0, -1, 1]
    
    # 현재 노드와 연결된 노드들 재귀적으로 방문
    for mr, mc in zip(mover, movec):
        mrow = r + mr
        mcol = c + mc
        
        # board의 범위를 넘어가는지 확인
        if mrow < 0 or mrow > (row - 1) or mcol < 0 or mcol > (col - 1):
            continue
        
        # 방문한 적 없는 알파벳이라면
        if board[mrow][mcol] not in chars:
            q.add((mrow, mcol, chars + board[mrow][mcol]))


print(moves)