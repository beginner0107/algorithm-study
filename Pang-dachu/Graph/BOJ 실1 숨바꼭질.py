import sys
from collections import deque

input = sys.stdin.readline

def BFS(N, K, location) :
    q = deque( [N] ) 

    while q :
        x = q.popleft()

        if x == K :
            return location[x]

        for i in (x-1, x+1, x*2) :
            if 0 <= i <= 100000 and not location[i] : 
                location[i] = location[x] + 1
                q.append(i)

N, K = map( int, input().split() )

location = [0] * 100001
print( BFS(N, K, location) )
 
