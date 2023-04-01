# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    
    score_dict = { x:y for x,y in zip(name, yearning) }
    
    answer = []
    
    for photo_one in photo :
        cross_name = [ x for x in name if x in photo_one ]
        
        temp = 0
        for i in cross_name :
            temp += score_dict[i]
        
        answer.append( temp )
    
    return answer
    
            