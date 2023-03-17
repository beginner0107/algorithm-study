# 입력 받기
row, col = map(int, input().split())    # row, col: 방의 행, 열
fr, fc, d = map(int, input().split())    # fr, fc: 처음 위치, d: 처음 바라보는 방향
room = [list(map(int, input().split())) for _ in range(row)]    # 벽 1, 청소한 영역 2로 표시할 리스트

# 청소하는 영역의 수 1로 초기화, 현재 위치 청소(2) 표시
cnt = 1
room[fr][fc] = 2

# 이동가능한 경우의 수 (바라보는 방향 d와 인덱스 연계)
# 0: 북(상), 1: 동(우), 2: 남(하), 3: 서(좌)
mr = [-1, 0, 1, 0]
mc = [0, 1, 0, -1]

while True:
    br, bc = fr, fc     # 현재 위치 저장
    # 바라보는 방향에서 90도를 돌고, 청소 안된 영역인지 확인
    for i in range(1, 5):
        # 반시계 방향 회전: 북->서->남->동
        # 인덱스가 줄어들어야 함
        dir = (d - i + 4) if (d - i) < 0 else (d - i)
        
        # 이동
        mvr = fr + mr[dir]
        mvc = fc + mc[dir]
        # 범위 안에 있고, 벽이 아니고, 청소 안된 부분이라면 -> 청소 표시(2), 이동, 청소 영역 늘려주기, 방향 변경
        if (0 < fr < row - 1) and (0 < fc < col - 1) and not room[mvr][mvc] :    
            room[mvr][mvc] = 2
            fr, fc = mvr, mvc
            cnt += 1
            d = dir
            break   
    
    # 청소를 아무 곳도 못 했다면, 뒤로 후퇴
    if (br == fr) and (bc == fc):
        fr -= mr[d]
        fc -= mc[d]
        if room[fr][fc] == 1:    # 벽에 도달했다면(1), 종료
            print(cnt)    # 결과 출력
            break