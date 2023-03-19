N, K = map(int, input().split())
tem = list(map(int, input().split()))

# 투 포인터 생성
left = 0
right = K-1
tem_sum = sum(tem[:K])
max_sum = tem_sum

while right < N-1:
    # 합에서 제일 앞의 값을 빼고 새로운 값 추가
    tem_sum += tem[right+1] - tem[left]  
    # 최대값 갱신
    max_sum = max(max_sum, tem_sum)  
    # 포인터 전환
    left = left + 1
    right = right + 1

print(max_sum)
