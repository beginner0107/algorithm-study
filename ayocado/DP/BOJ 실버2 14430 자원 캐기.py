import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
region = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = [[0] * M for _ in range(N)]

count[0][0] = region[0][0]
for row in range(N):
    for col in range(M):
        if row == 0 and col == 0:
            continue
        elif row == 0:
            if region[row][col] == 1:
                count[row][col] = count[row][col - 1] + 1
            else:
                count[row][col] = count[row][col - 1]
        elif col == 0:
            if region[row][col] == 1:
                count[row][col] = count[row - 1][col] + 1
            else:
                count[row][col] = count[row - 1][col]
        else:
            if region[row][col] == 1:
                count[row][col] = max(count[row][col - 1], count[row - 1][col]) + 1
            else:
                count[row][col] = max(count[row][col - 1], count[row - 1][col])
print(count[N - 1][M - 1])