import sys
from collections import deque

input = sys.stdin.readline

def BFS(N, K, location) :
    q = deque( [N] ) 

    while q :
        x = q.popleft()

        if x == K :
            return ( location[x]-1  )

        for i in (x-1, x+1, x*2) :
            if 0 <= i <= 100000 and not location[i] : 
                if i == x*2 :
                    location[i] = location[x]
                    q.appendleft( i )

                else : 
                    location[i] = location[x] + 1
                    q.append(i)

N, K = map( int, input().split() )

location = [0] * 100001

# 0초를 계산하는 경우가 있어서 그런듯 
location[N] = 1
print( BFS(N, K, location) )
 
