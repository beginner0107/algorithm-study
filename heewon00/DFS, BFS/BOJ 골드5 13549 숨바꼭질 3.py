from collections import deque

n, k = map(int, input().split())

INF=100001
dist = [INF] * INF

def dij(start):
    dist[start]=0
    queue = deque([start])

    while queue:
        v = queue.popleft()    
        nv = [v*2, v+1, v-1]
        
        for i in range(len(nv)):
            temp = nv[i]
            if 0<= temp <INF :
                #순간이동의 경우
                if i==0 and dist[temp] > dist[v]:
                    dist[temp] = dist[v]
                    queue.append(temp)

                #+1, -1의 경우
                elif i!=0 and dist[temp] > dist[v]+1:
                    dist[temp] = dist[v]+1
                    queue.append(temp)
    return dist[k]

print(dij(n))
