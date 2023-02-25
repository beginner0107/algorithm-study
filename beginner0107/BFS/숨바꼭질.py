import sys
from collections import deque
def bfs(s, target): # s: 수빈이의 시작 위치, target: 동생의 위치
    q = deque()     # bfs를 사용하기 위해 queue 자료구조 이용 
    q.append(s)   
    visited = [0] * 200001 # 이미 방문한 곳은 다시 방문할 필요 X
                           # 수빈이의 위치가 최대 100,000이므로 * 2하면 200,000 
    # s = 5 , target = 17
    # 너비: 0                5
    # 너비: 1            4  6  10
    # 너비: 2       3 8 7 12 9 11 20
    # 너비: 3    2 16 14 13 24 18 22 19 21
    # 너비: 4   1  15 17 32 -> 17발견
    while q:
        m = q.popleft() # m: 큐에서 꺼낸 변수
        if m == target: 
            return visited[m]
        else:
            for i in (m - 1, m + 1, m * 2):
                if 200001 > i >= 0 == visited[i]: # 범위 설정
                    visited[i] = visited[m] + 1   # 이전에 방문한 너비의 개수 + 1
                    q.append(i)                   # 큐에 넣어준다 

    return -1


n, k = map(int, sys.stdin.readline().split()) # n: 수빈이의 위치 , k 동생의 위치
ans = bfs(n, k) 
print(ans)