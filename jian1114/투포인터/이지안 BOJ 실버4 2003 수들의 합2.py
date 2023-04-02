N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= N and left <= right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)
    # 1. 합이 M이면 cnt+1, 오른쪽으로 한 칸
    if total == M:
        cnt += 1
        right += 1
    # 2. 합이 M 이하면 오른쪽으로 한 칸
    elif total < M:
        right += 1
    # 3. 합이 M 초과면 왼쪽꺼를 오른쪽 한 칸
    else:
        left += 1
print(cnt)