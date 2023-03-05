import sys

n = int(input())        # 값 입력

# 둘째줄 입력
A = sys.stdin.readline()
A = A.split(' ')

# 셋째줄 입력
B = sys.stdin.readline()
B = B.split(' ')

# 배열 정수화
for i in range(n) :
    A[i] = int(A[i])
    B[i] = int(B[i])

# A 내림차순, B 오름차순 정렬
A.sort(reverse = True)
B.sort()

# A와 B를 곱하여 답에 더 
cnt = 0
for i in range(n) :
    cnt = cnt + A[i] * B[i]

print(cnt)
