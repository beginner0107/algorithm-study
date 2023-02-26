"""
PGS 1844 게임 맵 최단거리
● 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
    게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서
    지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.
    단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

● 입출력 예시
    maps                                                            answer
    [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]   11
    [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]   -1

● 풀이 과정
1. 큐를 이용한 BFS
2. 큐에 [행, 열, step]을 push
3. 방문 여부에 대한 2차원 리스트 visited 만들기
4. popleft 후, 위,아래,왼쪽,오른쪽으로 이동할 수 있으면 이동한 [행,열,step]을 push
5. 이동한 행, 열의 visited 값 변경
6. 진행하다가 목적지에 도착하면 step값 return
7. popleft가 완료되어도 step이 return되지 않으면, return -1
"""
from collections import deque

def solution(maps):
    n = len(maps)     # 행의 개수
    m = len(maps[0])  # 열의 개수
    step = 1          # 이동한 칸 수

    if maps[n - 2][m - 1] == 0 and maps[n - 1][m - 2] == 0:  # 목적지 주변이 벽인 경우
        return -1
    else:
        row, col = 0, 0
        trace = deque()
        trace.append([row, col, step])         # 처음 [행, 열, step]을 큐에 저장
        visited = [[0] * m for _ in range(n)]  # 방문 여부 리스트 생성
        visited[0][0] = 1

        while trace:
            row, col, step = trace.popleft()

            if [row + 1, col] == [n - 1, m - 1] or [row, col + 1] == [n - 1, m - 1]:  # 한 번만 이동 시, 목적지에 도착할 경우
                step += 1
                return step
            else:
                if 0 <= row + 1 < n:  # 아래가 길이고, 방문하지 않았을 때
                    if maps[row + 1][col] and not visited[row + 1][col]:
                        trace.append([row + 1, col, step + 1])
                        visited[row + 1][col] = 1
                if 0 <= row - 1 < n:  # 위가 길이고, 방문하지 않았을 때
                    if maps[row - 1][col] and not visited[row - 1][col]:
                        trace.append([row - 1, col, step + 1])
                        visited[row - 1][col] = 1
                if 0 <= col + 1 < m:  # 오른쪽이 길이고, 방문하지 않았을 때
                    if maps[row][col + 1] and not visited[row][col + 1]:
                        trace.append([row, col + 1, step + 1])
                        visited[row][col + 1] = 1
                if 0 <= col - 1 < m:  # 왼쪽이 길이고, 방문하지 않았을 때
                    if maps[row][col - 1] and not visited[row][col - 1]:
                        trace.append([row, col - 1, step + 1])
                        visited[row][col - 1] = 1
        return -1