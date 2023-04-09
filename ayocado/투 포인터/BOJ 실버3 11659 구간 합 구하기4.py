import sys

N, M = map(int, sys.stdin.readline().split())

numList = list(map(int, sys.stdin.readline().split())) + [0]
sumList = [0]
SUM = 0
for i in range(N):
    SUM += numList[i]
    sumList.append(SUM)

answer = []
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    answer.append(sumList[end] - sumList[start - 1])

for i in range(M):
    if i == M - 1:
        print(answer[i], end = '')
    else:
        print(answer[i])