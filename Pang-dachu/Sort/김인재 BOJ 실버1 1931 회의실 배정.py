import sys

input = sys.stdin.readline

N = int(input())

time = [[0]*2 for _ in range(N)]

for i in range(N) :
    alpha, beta = map(int, input().split())
    
    time[i][0] = alpha
    time[i][1] = beta
    
time.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end_time = 0

for j in time :
    if j[0] >= end_time : 
        end_time = j[1]
        cnt += 1

print( cnt )