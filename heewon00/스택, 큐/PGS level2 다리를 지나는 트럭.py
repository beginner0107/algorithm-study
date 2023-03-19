def solution(bridge_length, weight, truck_weights):
    answer=1
    from collections import deque
    bridge=deque([0]*bridge_length)
    total=0
    for truck in range(len(truck_weights)):
        while True:
            removed=bridge[0]
            if total-removed+truck_weights[truck]>weight:
                bridge.popleft()
                bridge.append(0)
                total-=removed
                answer+=1
            else:
                break
        if truck==len(truck_weights)-1:
            answer+=bridge_length
            return answer
        total=total-bridge.popleft()+truck_weights[truck]
        bridge.append(truck_weights[truck])
        answer+=1
        
    return answer
