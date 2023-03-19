def solution(s):
    
    op=0
    cl=0
    
    if s.count(')')!=s.count('('):
        return False
    
    for i in s:
        if i=='(':
            op+=1
        else:
            cl+=1
        if op<cl:
            return False
        
    return True
