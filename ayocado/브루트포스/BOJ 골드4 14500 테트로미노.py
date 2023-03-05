"""
백준 14500 테트로미노

● 링크 : https://www.acmicpc.net/problem/14500

● 순서
1. 테트로미노가 만들어질 수 있는 모든 행, 열 이동 방법에 대한 리스트를 생성
2. for문을 이용하여 모든 점에서 [이동 방법]을 적용
3. 각 테트로미노의 합을 구하고, 리스트에 append
4. [모든 합의 경우]에서 최댓값(max) 출력

● 지정 변수
numbers : 쓰여진 숫자들에 대한 2차원 리스트
xx : 행이 이동할 수 있는 방법
yy : 열이 이동할 수 있는 방법
add : 하나의 테트로미노에 대한 합
adds : 모든 경우의 테트로미노에 대한 합들
next_row : 이동한 행 값
next_col : 이동한 열 값
"""
import sys

N, M = map(int, sys.stdin.readline().split())
numbers = []
for _ in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    numbers.append(x)

# 기준점에서 행, 열을 이동하는 방법(19가지)
# 순서 : 하늘(2가지), 노랑(1가지), 주황(8가지), 초록(4가지), 분홍(4가지)
xx = [[1, 2, 3], [0, 0, 0], [1, 1, 0], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, 1],
            [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 0, -1], [1, 1, 2], [0, -1, -1],
            [1, 1, 2], [0, 1, 1], [0, 0, 1], [1, 2, 1], [0, 0, -1], [1, 2, 1]]
yy = [[0, 0, 0], [1, 2, 3], [0, 1, 1], [0, 0, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2],
            [0, 0, -1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 1, 1], [1, 1, 2],
            [0, -1, -1], [1, 1, 2], [1, 2, 1], [0, 0, 1], [1, 2, 1], [0, 0, -1]]

add = 0   # 한 가지 테트로미노의 합
adds = [] # 모든 경우 테트로미노의 합

# row, col로 기준점 이동
for row in range(N):
    for col in range(M):
        # xx, yy 적용
        for i in range(len(xx)):
            count = 1
            add = numbers[row][col]
            for j in range(3):
                next_row = row+xx[i][j]  # 새로운 행
                next_col = col+yy[i][j]  # 새로운 열
                if 0 <= next_row < N and 0 <= next_col < M:
                    add += numbers[next_row][next_col]
                    count += 1
                else:
                    break
            # 하나의 테트로미노에서 세 번의 이동을 만족할 경우 adds에 추가
            if count == 4:
                adds.append(add)
print(max(adds)) # 최댓값 출력