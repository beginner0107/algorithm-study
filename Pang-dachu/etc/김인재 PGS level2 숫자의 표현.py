# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n) :
    count = 0 
    for i in range(1, n+1):
        temp = n
        
        for j in range(i, n+1) :
            temp -= j
            
            if temp == 0 : 
                count += 1
                break
            elif temp < 0 : 
                break
    return count 