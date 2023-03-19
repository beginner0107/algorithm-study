from collections import deque

def solution(priorities, location):
    cnt = 0
    prior = deque([(J,idx) for idx,J in enumerate(priorities)])
    
    while prior:
        J,idx = prior.popleft()
        if prior and max(prior)[0] > J :
            prior.append((J,idx))
        else:
            cnt+=1
            if idx==location:
                break
    return cnt
