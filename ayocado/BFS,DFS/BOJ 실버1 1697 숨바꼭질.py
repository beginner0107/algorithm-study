import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

time = [float('inf')] * 200000
move = [-1, 1, 2]

point = deque()
point.append(N)  # 첫 시작 위치
time[N] = 0  # 시작 위치 시간 수정
while point:
    currentPoint = point.popleft()

    if currentPoint == K:
        break
    for i in move:
        if i == 2:
            nextPoint = currentPoint * i
        else:
            nextPoint = currentPoint + i
        if 0 <= nextPoint < 200000:
            if time[currentPoint] + 1 < time[nextPoint]:
                time[nextPoint] = time[currentPoint] + 1
                point.append(nextPoint)

print(time[currentPoint])