import math, sys

def combination(n, m):
    return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))

t = int(sys.stdin.readline())  # 테스트 케이스의 개수 입력

ans = []

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())  # n과 m 입력
    result = combination(n, m)
    ans.append(result)

for k in ans :
    print(k)
