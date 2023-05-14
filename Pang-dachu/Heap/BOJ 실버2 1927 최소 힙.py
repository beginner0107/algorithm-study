# https://www.acmicpc.net/problem/1927

import sys
import heapq
input = sys.stdin.readline

N = int(input())

min_heap = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, x)