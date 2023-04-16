import sys
input =sys.stdin.readline

n = int(input())
m = int(input())
t = 0

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#dfs
def dfs(idx):
    global visited,t
    visited[idx] = True
    t += 1
    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
            
    
dfs(1)
print(t-1)