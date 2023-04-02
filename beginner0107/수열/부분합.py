import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum = 0
ans = sys.maxsize
q = []
for i in range(N):
    sum += arr[i]
    q.append(arr[i])
    while sum >= S:
        ans = min(ans, len(q))
        sum -= q.pop(0)

if ans == sys.maxsize:
    print(0)
else:
    print(ans)
