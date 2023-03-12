from itertools import permutations

def solution(k, dungeons):
    answer = []
    temp = list( permutations(dungeons, len(dungeons)) )
    
    for dun in temp :
        cnt = 0
        temp_k = k
        
        for i in dun :
            if temp_k >= i[0] :
                temp_k -= i[1]
                cnt += 1
        answer.append(cnt)
    
    return max(answer) 
    
    
    
