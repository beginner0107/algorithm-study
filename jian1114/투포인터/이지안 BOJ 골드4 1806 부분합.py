## 투 포인터
import sys
#input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

start, end = 0, 0 
partial_sum = seq[0]
answer = 100001

while end < N:
    ## 1. 부분합이 S 이상인 경우, 
    if partial_sum >= S:
        answer = min(answer, end - start + 1)
        # 현재까지의 부분합에서 시작지점 값을 빼주고, 시작지점을 오른쪽으로 한 칸 옮긴다
        partial_sum -= seq[start]
        start += 1
    ## 2. 부분합이 S 미만인 경우,
    else:
        # 끝나는 지점을 오른쪽 한 칸 옮겨주고, 수열을 벗어나지 않았다면
        # 해당 값을 더해준다.
        end += 1
        if end < N:
            partial_sum += seq[end]

if answer == 100001:
    print(0)
else:
    print(answer)