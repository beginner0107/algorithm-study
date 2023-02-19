import sys
input = sys.stdin.readline

N = int(input())


# 스택 기본 용어 및 기능 

stack = []
for _ in range(N):
    s = input().split()
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif (s[0] == 'pop') & (len(stack) != 0):
        print(stack.pop())
    elif (s[0] == 'pop') & (len(stack) == 0):
        print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif (s[0] == 'empty') & (len(stack) == 0):
        print(1)
    elif (s[0] == 'empty') & (len(stack) != 0):
        print(0)
    elif len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])