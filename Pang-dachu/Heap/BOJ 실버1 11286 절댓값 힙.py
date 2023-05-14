# https://www.acmicpc.net/problem/11286

import sys, heapq

abs_heap = []
n = int(sys.stdin.readline())
for i in range(n):
	x = int(sys.stdin.readline())
	if x:
		heapq.heappush(abs_heap, (abs(x), x))
	else:
		if abs_heap:
			print(heapq.heappop(abs_heap)[1])
		else:
			print(0)