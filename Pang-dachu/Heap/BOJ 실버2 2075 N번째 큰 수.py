# https://www.acmicpc.net/problem/2075 

import heapq

heap = []
n = int(input())

for _ in range(n):
    table = map(int, input().split())
    for i in table:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])