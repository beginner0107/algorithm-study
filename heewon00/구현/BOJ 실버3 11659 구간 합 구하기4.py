import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #수의 개수, 합 횟수
lst = list(map(int, input().split()))

lstsum=[0]
numsum=0

for i in range(n):
    numsum += lst[i]
    lstsum.append(numsum)

for _ in range(m):
    a,b = map(int,input().split())
    print(lstsum[b]-lstsum[a-1])
