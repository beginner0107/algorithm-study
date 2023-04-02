'''
stack 문제

stack이 비어있으면 append
stack의 top 원소(peek)랑 s문자열 현재 index랑 같으면 stack pop
두 경우도 해당 되지 않으면 append
'''

def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) == 0:
        return 1
                
    return 0