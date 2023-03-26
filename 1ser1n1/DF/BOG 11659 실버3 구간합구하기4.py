import sys
input = sys.stdin.readline

N, M = map(int, input().split())

#인덱스 맞춰주기 위해 0을 맨 앞에 추가
num = [0] + list(map(int, input().split()))
sum_num = [0]*(N+1) 

#구간합 리스트
for i in range(1, N+1):
    if i == 1:
        sum_num[i] = num[i]
    else:
        sum_num[i] = sum_num[i-1] + num[i]
        
#구간합 리스트
for i in range(M):
    s, e = map(int, input().split())
    print(sum_num[e]-sum_num[s]+num[s])