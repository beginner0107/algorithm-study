def solution(s):
    stack = [] 		#스택(리스트) 선언
    for i in range(len(s)) :	
        if s[i]=='(' :		    #문자가 '('이면
            stack.append('(')	#push('(')
        else :		            #문자가 ')'이면
            if len(stack)==0 :	#isEmpty(), 스택이 비었는데
                return False	#')'가 들어왔다면 거짓
            stack.pop()		    #아니라면 '(' 제거
    if len(stack)==0 :		    #isEmpty()
        return True		        #남은 '('가 없다면 참
    else :
        return False		    #무엇이든 남았다면 거짓