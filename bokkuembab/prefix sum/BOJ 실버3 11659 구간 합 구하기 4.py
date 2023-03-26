# 구간합은 누적합을 구한 후, 구간의 값을 빼주면 됨
import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n: 수의 개수, m: 합을 구해야 하는 횟수
nums = list(map(int, input().split()))    # 합을 구할 숫자들
prefix_sum = [0]    # 누적합을 저장할 리스트
for i in range(n):
    prefix_sum.append(prefix_sum[i] + nums[i])

for _ in range(m):
    i, j = map(int, input().split())
    # [i, j] 구간의 합 구하기
    print(prefix_sum[j] - prefix_sum[i - 1])