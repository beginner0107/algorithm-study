import sys
from collections import deque
#input = sys.stdin.readline

def bfs(v):
    q = deque([v])

    # 모든 경우를 탐색
    while q:
        v = q.popleft()
        if v == K:
            return visited[v]
        
        for i in (v-1, v+1, 2*v):
            if (0 <= i <= 100000) and visited[i] == -1:
                # 1. 순간이동
                if i == 2*v:
                    visited[i] = visited[v]       # 0초
                    q.appendleft(i)               # 순간이동 한 후에 바로 이동
                # 2. 걷기
                else:
                    visited[i] = visited[v] + 1   # 1초
                    q.append(i)                  
                
N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]
visited[N] = 0
print(bfs(N))