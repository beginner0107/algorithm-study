import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split( )))

# 누적합 리스트를 미리 구한다.
for i in range(N-1):
    arr[i+1] += arr[i]
arr = [0] + arr

for _ in range(M):
    a, b = map(int, input().split())
    print(arr[b] - arr[a-1])


'''
# 시간초과 코드
N, M = map(int, input().split())
arr = list(map(int, input().split( )))
for _ in range(M):
    ans = 0
    a, b = map(int, input().split( ))
    for i in range(a, b+1):
        ans += arr[i-1]
    print(ans)
'''