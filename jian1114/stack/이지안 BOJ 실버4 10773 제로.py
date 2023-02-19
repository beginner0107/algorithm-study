import sys
input = sys.stdin.readline

K = int(input())

# stack을 쌓을 빈 리스트 생성
stack = []
for _ in range(K):
    n = int(input())
    
    # 0인 경우, 스택에서 가장 위에 있는 수 제거
    if n == 0:
        stack.pop()

    # 0이 아닌 경우, 스택에 추가
    else:
        stack.append(n)

# 스택 합
print(sum(stack))