from collections import deque

def solution(priorities, location):
    cnt = 1
    
    pri = [(j,i) for i,j in enumerate(priorities)]
    pri = deque( pri )

    max_value = max(pri)[0]
    while pri :
        temp = pri.popleft()

        if temp[0] == max_value :         
            if temp[1] == location :
                return cnt
            
            max_value = max(pri)[0]
            cnt += 1
        
        else : 
            pri.append(temp)