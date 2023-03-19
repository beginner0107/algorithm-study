# 변수 입력
N, M =  map(int, input().split())
A = []
for i in range(N) :
    A.append(int(input()))

A.sort()

# 투 포인터, 답을 받기 위해 최대값 입력
left, right = 0, 1
ans = A[N-1]*2

# N보다 작으면 계속
while left < N and right < N:
    diff = A[right] - A[left] # 차이값을 비교
    if diff >= M:
        ans = min(ans, diff)
        left = left + 1
    else:
        right = right + 1

print(ans)

