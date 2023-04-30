
def solution(k, dungeons):
    from itertools import permutations
    result=0
    
    for 던전순서 in permutations(dungeons):
        던전수=0 ; 현재체력=k
        for 필요,소모 in 던전순서:
            if 현재체력>=필요:
                현재체력-=소모
                던전수+=1
            else:
                if 던전수>result:
                    result=던전수
                break
        if 던전수>result:
            result=던전수
    return result
            
        
