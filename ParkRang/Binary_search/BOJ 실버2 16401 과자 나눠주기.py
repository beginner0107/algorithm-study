M, N = map(int, input().split())    # 조카 수 / 막대 과자 갯수
s = list(map(int, input().split())) # 과자 길이

start = 0           # 가장 작은 길이
end = max(s)        # 가장 큰 길이

MAX = 0
while start <= end: # 이진 탐색
    count = 0       # 수 세기
    mid = (start + end)//2

    if mid < 1:     # 줄 수 없을 시 종료
        break

    # 과자 갯수 만큼 반복, 과자에서 나올 수 있는 갯수 저장
    for i in range(N) :
        if s[i]>=mid:
            count = count + s[i]//mid
    # 갯수가 같으면 최대길이 저장, 종료/아니면 범위 감소
    if count == M :
        MAX = mid
        break
    elif count > M:
        MAX = mid
        start = mid + 1
    else :
        end = mid - 1

# 최대 길이 
print(MAX)
