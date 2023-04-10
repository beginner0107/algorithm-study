import sys
input = sys.stdin.readline

# 입력 받기
got, target = map(int, input().split())    # got: 갖고 있는 랜선의 수, need: 필요한 랜선의 수
lans = []
for _ in range(got):
    lans.append(int(input()))

left, right = 0, max(lans) + 1
while left < right:
    mid = (left + right) // 2   # 자르는 단위
    
    nums = 0    # 나눴을 때의 개수
    for l in lans:
        nums += l // mid    # 단위로 잘랐을 때의 개수
        
    if nums < target:    # 개수가 너무 적으면 (단위가 너무 크면)
        right = mid  
    else:    # 단위가 너무 작으면
        left = mid + 1
        
print(right - 1)