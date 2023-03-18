from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
col, row, hei = map(int, input().split())    # col, row, hei: 가로, 세로, 높이
box = [[list(map(int, input().split())) for _ in range(row)] for _ in range(hei)]    # 토마토 정보가 담긴 리스트 초기화

# 익은 토마토가 영향을 주는 범위 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향)
eff_h = [-1, 1, 0, 0, 0, 0]    # 상하
eff_r = [0, 0, 0, 0, -1, 1]    # 전후
eff_c = [0, 0, -1, 1, 0, 0]    # 좌우

# 한 상자에 익은 토마토가 여러 개 있을 수 있으므로, 익은 토마토를 모두 찾아 큐에 넣기
q = deque()    # 큐 선언
for h in range(hei):    # 익은 토마토 찾아서 큐에 넣기
    for r in range(row):
        for c in range(col):
            if box[h][r][c] == 1:
                q.append((h, r, c, 0))    # 마지막 숫자는 모두 익은 토마토로 만드는 데 걸린 시간
                
while q:
    h, r, c, cnt = q.popleft()    # 큐에서 값 꺼내기
    
    # 토마토 영향을 주는 범위대로 익게 하기
    for effect_h, effect_r, effect_c in zip(eff_h, eff_r, eff_c):
        eh = h + effect_h
        er = r + effect_r
        ec = c + effect_c
        
        if (0 <= eh < hei) and (0 <= er < row) and (0 <= ec < col):    # box 범위를 넘어가지 않고,
            if not box[eh][er][ec]:    # 익지 않은 토마토가 있다면
                box[eh][er][ec] = 1    # 토마토 익은거 표시하고,
                q.append((eh, er, ec, cnt + 1))    # q에 넣어주기 (cnt는 다음날로 넘어가기)

# 토마토가 모두 익지 못한다면, -1 출력
for h in range(hei):
    for r in range(row):
        for c in range(col):
            if not box[h][r][c]:
                cnt = -1
                break

# 정답 출력
print(cnt)