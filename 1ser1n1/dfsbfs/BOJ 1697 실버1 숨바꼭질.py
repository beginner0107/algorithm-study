import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, e):
    q = deque()
    v = [0] * 200001
    
    #초기 데이터 삽입, v[]초기화
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.popleft()
        if c == e:
            return v[e]-1
        #3방향, 범위내(0~200000), 미방문
        for n in (c-1, c+1, c*2):
            if 0<=n<=200000 and v[n] == 0:
                q.append(n)
                v[n] = v[c]+1
                
    return -1
    

S, E = map(int,input().split())
ans = bfs(S, E)
print(ans)