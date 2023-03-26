'''
투 포인터 알고리즘 참조
-> 이분 탐색이랑 비슷한 구조
'''

import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum = [0] * (n+1)
for i in range(1, n+1):
    sum[i] = sum[i-1] + arr[i-1]

answer = 100001
# left, right는 sum 리스트의 인덱스를 가르키는 요소
left = 0
right = 1

# else: right를 계속 늘려가면서 그 구간의 부분합이 s보다 크거나 작을 때 까지
#       right가 구간 끝까지 가면 left+1
# left = n 일 때 while문 break
while left != n:
    if sum[right] - sum[left] >= s:
        # 최솟값 갱신
        answer = min(right-left, answer)
        left += 1
    else:
        if right != n:
            right += 1
        else:
            left += 1
            
print(answer if answer != 100001 else 0)