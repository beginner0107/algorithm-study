# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램
# ===>구간합 + 투포인터

# 입력 받기
n, s = map(int, input().split())    # n: 수열의 길이, s: 부분합의 기준(s 이상)
nums = list(map(int, input().split()))    # 수열 리스트

# 초기값 설정
res = int(1e9)    # s이상 부분합의 구간 길이 최소값 (최대값으로 초기화)
pref = [0] * (n + 1)    # 누적합 리스트
for i in range(n):
    pref[i + 1] = pref[i] + nums[i]

left, right = 0, 1    # 좌, 우 포인터
while left < right:    # 우 포인터가 좌 포인터보다 큰 동안에
    if right > n:    # 우 포인터가 수열 리스트의 범위를 넘어가면 종료
        break
    
    if pref[right] - pref[left] >= s:    # 부분합이 s 이상이면, 
        res = min(res, right - left)    # 기존 최소 구간과 비교해 작은 구간으로 갱신
        left += 1    # 좌 포인터 오른쪽으로 한 칸 옮기기 (부분합 줄이기)
    else:    # 부분합이 s보다 작으면,
        right += 1    # 우 포인터를 오른쪽으로 한 칸 옮기기 (부분합 늘리기)
    
print(res if res != int(1e9) else 0)