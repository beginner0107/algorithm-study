# https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    
    price = deque( prices )
    answer = []
    

    while True :
        if not price : 
            break 
            
        item = price.popleft()
        cnt = 0
        
        for i in price :
            cnt += 1
            if item <= i :
                continue
            else :
                break
            
        answer.append( cnt )
        
    return answer 
        
        
    