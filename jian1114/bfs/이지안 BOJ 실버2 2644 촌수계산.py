from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a,b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)   

def BFS(s):
    queue = deque([s])
    visited[s] = True

    # 큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:     
            if not visited[i]:
                queue.append(i)
                answer[i] = answer[v] + 1
                visited[i] = True

visited = [False] * (n + 1)
answer = [0] * (n + 1)
BFS(a)

if answer[b] > 0 :
    print(answer[b])
else:
    print(-1)