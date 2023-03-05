from collections import deque 

def solution(priorities, location):
    
    # (우선순위, 인덱스)로 deque에 저장
    q = deque([(v,i) for i,v in enumerate(priorities)])
        
    answer = 0
    
    while q:
        item = q.popleft()
        # q가 비어있지 않고 우선순위가 가장 먼저인 value보다 q.popleft한 값이 작으면
        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    
    return answer