import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    num = int(input())
    l.append(num)
    
stack = []
cunt = 0
answer = ""

for i in range(1, n+1):
    stack.append(i)
    answer += "+"
    #현재 스택의 최상단이 구현하려는 수열과 같을때
    while stack and stack[-1] == l[cunt]:
        stack.pop()
        answer += "-"
        cunt += 1


if stack:
    print("NO")
else:
    for _ in answer:
        print(_)
