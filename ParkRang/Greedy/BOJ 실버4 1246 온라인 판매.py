N, M = list(map(int, input().split()))  # N, M 입력

arr = []    # 값을 저장할 배열
val = 0     # 가장 높은 가격을 저장할 값
cnt = 0     # 판매 수량
MAX = 0     # 최대 총 가격
MAX_cnt = 0 # 최대 판매 갯수

# 배열에 값 입력
for i in range(M) :
    P = int(input())
    arr.append(P)

# 배열 정렬
arr.sort()

# M-1부터 1까지의 값을 검사
for i in range(1,M) :
    cnt = cnt + 1               # 판매 수량
    if cnt > N :                # 가진 수보다 많으면 최대량 고정
        cnt = N
    if MAX <= arr[M-i] * cnt :  # 최대 총 가격 비교
        MAX = arr[M-i] * cnt    # 최대 총 가격 저장
        val = arr[M-i]          # 최대 가격
        MAX_cnt = cnt           # 최대 판매량

print(val, val*MAX_cnt)         # 값 리턴


