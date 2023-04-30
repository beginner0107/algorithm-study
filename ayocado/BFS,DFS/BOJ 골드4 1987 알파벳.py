import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]

# 리스트에서 set 자료형으로 변경 > 시간초과 통과
# set 시간복잡도 : O(1), list 시간복잡도 : O(n)
stack = set([(0, 0, 1, board[0][0])])

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]

maxDist = 1
while stack:
    row, col, dist, alphabet = stack.pop()
    
    for i in range(4):
        newRow = row + xx[i]
        newCol = col + yy[i]
        if 0 <= newRow < R and 0 <= newCol < C:
            if board[newRow][newCol] not in alphabet:
                newAlphabet = alphabet + board[newRow][newCol]
                stack.add((newRow, newCol, dist + 1, newAlphabet))
                if dist + 1 > maxDist:
                    maxDist = dist + 1

print(maxDist)
