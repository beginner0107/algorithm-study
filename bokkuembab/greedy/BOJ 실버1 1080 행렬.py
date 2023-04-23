# 행렬 A->B로의 변환 횟수의 최소값 구하기 (변환 불가능 -> -1 출력)
# 3*3 크기의 부분 행렬의 모든 원소를 토글함
# 3*3 크기보다 작은데, 다른 요소가 있다 -> 변경 불가
# 행, 열의 길이는 50이하의 자연수 -> 단순 반복 가능

import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())    # 행렬의 크기 (50이하의 자연수)
ali = [list(map(int, input().rstrip())) for _ in range(n)]    # 행렬 A
bli = [list(map(int, input().rstrip())) for _ in range(n)]    # 행렬 B


# 초기화
ans = 0    # 토글 횟수를 0으로 초기화

# 3*3 행렬 뒤집는 함수 생성
def flip_33(sr, sc):
    for row in range(sr, sr + 3):
        for col in range(sc, sc + 3):
            ali[row][col] = 1 - ali[row][col]

# 3*3 크기보다 작은데, 다른 요소가 있는지 먼저 고려
#### 해당 부분 없어도 range 범위에서 돌아가지 않고, 마지막 ali==bli 출력 확인에서 고려됨

# 3*3 크기로 한 칸씩 옮겨가며 확인
for row in range(n - 2):    # 행 방향 이동 가능 횟수
    for col in range(m - 2):    # 열 방향 이동 가능 횟수
        if ali[row][col] != bli[row][col]:    # 3*3의 첫번째 요소가 같지 않다면,
            flip_33(row, col)    # 3*3 부분 행렬 뒤집고,
            ans += 1    # 횟수 늘려주기
            
        if ali == bli:
            break
    if ali == bli:
        break   

# 결과 출력
if ali == bli:    # 전체를 돌면서 토글했을 때 같다면
    print(ans)    # 횟수 출력
else:    # 다르다면
    print(-1)    # -1 출력