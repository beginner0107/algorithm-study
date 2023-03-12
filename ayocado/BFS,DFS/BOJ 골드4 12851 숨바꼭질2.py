import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

time = [float('inf')] * 200000
queue = deque()

time[N] = 0
queue.append([N, 0])
move = [-1, 1, 2]
answer = 0
while queue:
    # print(queue)
    currentPoint, spendTime = queue.popleft()
    # print('currentPoint : ', currentPoint, ' spendTime: ', spendTime, ' answer : ', answer)
    if currentPoint == K:
        if answer == 0:
            answer += 1
            shortestTime = spendTime
            continue
    if answer > 0:
        if spendTime > shortestTime:
            break
        else:
            if currentPoint == K:
                answer += 1
            continue
    for i in move:
        if i == 2:
            nextPoint = currentPoint * i
        else:
            nextPoint = currentPoint + i
        if 0 <= nextPoint < 200000:
            if time[nextPoint] >= time[currentPoint] + 1:
                queue.append([nextPoint, time[currentPoint] + 1])
                time[nextPoint] = time[currentPoint] + 1

if len(queue) == 0:
    print(spendTime)
    print(answer)
else:
    print(spendTime - 1)
    print(answer)