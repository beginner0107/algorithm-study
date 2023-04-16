def balance(text):
    op=0; cl=0; idx=0
    for t in text:
        idx+=1
        if t=="(":op+=1
        else: cl+=1
        if op==cl:
            return text[:idx], text[idx:]

def correct(text):
    op=0; cl=0
    for t in text:
        if t=="(":op+=1
        else: cl+=1
        if op<cl:
            return False
    return True

dic={'(':')', ')':'('}

def gwal(text):
    if not text:
        return text
    
    u,v=balance(text)
    
    if correct(u): 
        return u+gwal(v)
    else:
        new_u=''.join([dic[i] for i in u[1:-1]])
        return '('+gwal(v)+')'+new_u

def solution(p):
    return gwal(p)
