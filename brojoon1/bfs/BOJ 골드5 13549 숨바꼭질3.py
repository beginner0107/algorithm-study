"""
# BOJ 13549 숨바꼭질3
수빈이 N, 동생 K ( 0 <= N, K <= 100,000)
수빈이는 1초에 +1, -1이동 / 순간이동 시 !!![0 초]!!! 에 *2
수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 출력 

"""
def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        
        # 종료조건
        if x == K:
            print(graph[x])
            break
        
        # 3방향에 대한 for문
        for i in range(3):
            # *2 일 때
            if i == 2:
                nx = x * dx[i]
            # -1 or +1 일 때
            else:
                nx = x + dx[i]
            
            # nx가 범위 내에 있고, 들리지 않았으면
            if 0 <= nx < 100001 and graph[nx] == 0:
                # *2 일 때 조건
                # 순간이동을 하면 0초에 *2를 가므로 +1 할 필요 없음
                if nx == x * 2 and x != 0:
                    graph[nx] = graph[x]
                    q.appendleft(nx)
                # -1 or 1 일 때
                else:
                    graph[nx] = graph[x] + 1
                    q.append(nx)

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
graph = [0] * 100001

dx = [-1, 1, 2]

bfs(N)