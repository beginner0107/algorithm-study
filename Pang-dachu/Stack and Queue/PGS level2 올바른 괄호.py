def solution(s):
    
    stack = []
    
    for i in s :
        stack.append( i )
        
        if len(stack) == 0 or len(stack) == 1 :
            continue
        
        if stack[-2] == '(' and stack[-2] != stack[-1] :
            stack.pop()
            stack.pop()
    
    return True if len(stack) == 0 else False