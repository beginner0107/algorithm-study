import sys
input = sys.stdin.readline

n = int(input())    # 전체 용액의 수
li = list(map(int, input().split()))    # 용액의 특성값 리스트

left, right = 0, n - 1

# 양쪽 끝 수를 더한 것으로 정답 초기화
ans = abs(li[left] + li[right])
ans_L, ans_R = left, right

while left < right:    # left와 right는 다른 수를 가리켜야 함
    check = li[left] + li[right]
    
    if abs(check) < ans:    # 기존 정답보다 작으면,
        ans = abs(check)
        ans_L, ans_R = left, right
        
        if ans == 0:    # 두 수의 합이 0이 되면, 종료
            break
        
    if check < 0:    # 두 수의 합이 음수이면, (음수 값이 크다는 뜻)
        left += 1     # 더 작은 음수 선택
    else:    # 두 수의 합이 양수이면, (양수 값이 크다는 뜻)
        right -= 1    # 더 작은 양수 선택

print(li[ans_L], li[ans_R])