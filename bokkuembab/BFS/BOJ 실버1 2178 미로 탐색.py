from collections import deque
import sys
input = sys.stdin.readline

# BFS 함수
def bfs(graph, visited, tr, tc):
    
    # 이동할 수 있는 경우의 수 (상, 하, 좌, 우)
    mr = [-1, 1, 0, 0]
    mc = [0, 0, -1, 1]
    
    # 1. queue 선언 및 방문 처리
    queue = deque([(0, 0, 0)])
    visited[0][0] = True
    
    # 2. 큐가 빌 때까지 반복
    while queue:
        # 3. 큐에서 요소 빼서 출력
        r, c, cnt = queue.popleft()
        
        # 4. 목표 위치에 도달했으면, 종료
        if r == (tr - 1) and c == (tc - 1):
            return cnt
        
        # 5. 이동 가능한 모든 경우의 수 방문
        for moveR, moveC in zip(mr, mc):
            row = r + moveR
            col = c + moveC
            if (row >= tr) or (row < 0) or (col >= tc) or (col < 0):    # 범위를 벗어나면, 넘어가기
                continue
            
            # 6. 방문하지 않았고, 갈 수 있는 위치라면, queue에 삽입 및 방문 처리
            if not visited[row][col] and graph[row][col] == 1:    
                queue.append((row, col, cnt + 1))
                visited[row][col] = True

            
                
# row, col: 이동할 끝좌표
row, col = map(int, input().split())
mapli = []

# 지도 입력받기
for r in range(row):
    str = list(input().strip())
    mapli.append(list(map(int, str)))
    
visited = [[False] * col for _ in range(row)]

print(bfs(mapli, visited, row, col) + 1)    # 마지막 이동횟수 더해주고 출력