import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

li = []
sum = 0
q = []
for i in range(N):
    sum += arr[i]
    q.append(arr[i])
    while sum >= S:
        li.append(len(q))
        sum -= q.pop(0)

li.sort()
if not li:
    print(0)
else:
    print(li[0])
