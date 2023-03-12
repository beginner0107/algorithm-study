import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_n = [int(x) for x in input().split()] #원본 배열
list_sum = [0] * n#구간합 배열 담을 공간
C = [0] * m #같은 나머지의 인덱스를 카운트하는 리스트
answer = 0

#구간합 배열 저장
for i in range(0, n):
    if i == 0:
        list_sum[i] = list_n[i]
    else:    
        list_sum[i] = list_sum[i-1] + list_n[i]

for i in range(n):
    remainder = list_sum[i] % m
    #나머지가 0이라면 정답 값 증가
    if remainder == 0:
        answer += 1
    C[remainder] += 1 #모든 나머지 경우의수 갯수 저장

#C 배열 탐색
for i in range(m):
    #같은 나머지를 같는 수가 2개 이상이면
    if C[i] > 1:
        answer += (C[i]*(C[i]-1)//2) #나머지 개수에서 2가지 뽑는 경우의 수

print(answer)

