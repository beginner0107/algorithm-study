
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    Q = input()
    if "push" in Q:
        Q, num = Q.split(" ")
        stack.append(int(num))
        
    if Q == "top\n":
        print(stack[-1] if stack else -1)
        
    if Q == "size\n":
        print(len(stack))
        
    if Q == "empty\n":
        print(0 if stack else 1)
        
    if Q == "pop\n":
        print(stack.pop() if stack else -1)