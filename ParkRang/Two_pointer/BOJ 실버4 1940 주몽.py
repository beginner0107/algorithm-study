N = int(input())
M = int(input())
num = list(map(int, input().split()))

num.sort()
cnt = 0

# 투 포인터
left, right = 0, N-1

# 포인터가 제대로 되었을 시 계속
while left < right :
    armor = num[left] + num[right] # 배열의 값으로 생성
    if armor < M : # M보다 작으면 증가
        left = left + 1
    elif armor > M : # M보다 크면 감소
        right = right - 1
    else :  # 적정시 카운트 증가, 범위 변환
        cnt = cnt + 1
        left = left + 1
        right = right - 1

print(cnt)
