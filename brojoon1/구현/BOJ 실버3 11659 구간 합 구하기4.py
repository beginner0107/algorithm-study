'''
5 4 3 2 1

5 / 5+4 / 5+4+3 / 5+4+3+2 / 5+4+3+2+1
2~4번째 구간 합 => 4 - 1

'''

import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
# 0을 넣어주는 이유 idx 편하게 다룰려고
sum = [0]

tmp = 0
for i in arr:
    tmp += i
    sum.append(tmp)
# print(sum)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(sum[end] - sum[start-1])



'''
# 시간 초과 코드
# 이유: 파이썬은 1초에 2000만번 연산 가능
# n,m은 1~10만 
# 10만 x 10만 = 100억   => 시간초과


n, m = map(int, input().split())

arr = list(map(int, input().split()))
answer = []

for i in range(m):
    start, end = map(int, input().split())
    sum = 0
    for j in range(start-1, end):
        sum += arr[j]
    
    answer.append(sum)
    
for i in answer:
    print(i)
'''

