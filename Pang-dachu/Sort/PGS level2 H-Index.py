def solution(citations):
    if sum(citations) == 0 :
        return 0
    num = sorted([i for i in range(0, max(citations)+1)])
    
    for i in range( len(num) ) :
        
        temp = list(map(lambda x : 1 if x >= num[i] else 0 , citations))
        
        if temp.count(1) >= num[i] and temp.count(0) <= num[i] :
            continue
        
        
        return num[i-1]
        
        
    