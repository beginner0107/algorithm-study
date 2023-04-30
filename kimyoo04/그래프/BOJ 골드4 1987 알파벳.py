# https://www.acmicpc.net/problem/1987

"""
문제
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1
2 4
CAAB
ADCB

예제 출력 1
3
"""

"""
핵심
- visited를 통해 지금까지 지나온 알파벳과 다르게 하기 + set 자료형 사용
- 깊이 우선 탐색으로 트리 깊이를 cnt로 사용 -> 최대 몇 칸 지나기 가능? (처음 칸도 포함)
- 상하좌우 이동
- global 사용
"""

import sys; input=sys.stdin.readline
from collections import deque

# 입력값 처리
R, C = map(int, input().split()) # R 세로, C 가로

# 시간초과를 없애기 위한 문자를 숫자로 변환
# graph = [list(input().strip()) for _ in range(R)] # 보드
graph = [list(map(lambda a : ord(a)-65,input())) for _ in range(R)]

max_ = 1 # 최대 말 이동 칸 수

# 상하좌우
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

# 방문노드
visited = [0 for _ in range(26)]


# 재귀 방식으로 트리깊이가 깊어질 때 cnt 증가
def dfs(x,y,cnt):
    global max_
    if max_ < cnt:
        max_ = cnt

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]
        # 문자열 처리하니까 시간초과가 난다 알파벳개수만 큼 리스트 만들어서
        if 0 <= nx < R and 0 <= ny < C and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            visited[graph[nx][ny]] = 0

max_ = 1

visited[graph[0][0]] = 1
dfs(0,0,max_)
print(max_)


"""
def bfs():
    global max_
    visited = set(graph[0][0])
    q = deque([])
    q.append((0, 0, visited))
    # 방문노드

    while q:
        nx, ny, visited = q.popleft()

        # 말이 지날 수 있는 최대의 칸 초기화
        max_ = max(max_, len(visited))

        for i in range(4):
            x = nx + mx[i]
            y = ny + my[i]

            if 0 <= x < C and 0 <= y < R and graph[y][x] not in visited:
                visited.add(graph[y][x])
                q.append((nx, ny, visited))

    return max_

print(bfs())
"""