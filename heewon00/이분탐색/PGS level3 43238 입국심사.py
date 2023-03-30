def solution(n, times):
    # n : 입국심사를 기다리는 사람 수
    # times : 각 심사관이 한 명을 심사하는데 걸리는 시간
    
    left = min(times) #최소 : 1명이 가장 빠른 심사관에게 감
    right = max(times)*n #최대 : n명이 가장 느린 심사관에게 감
    
    while left<=right:
        mid = (left + right) // 2 #중앙값의 시간
        
        #중앙값일 때 심사 가능한 사람 수를 계산한다.
        mid_person = 0 
        for time in times:
            mid_person += mid//time
            #모든 심사관을 거치지 않아도 mid분 동안 n명보다 많은 사람을 심사한다면 for문 탈출
            if mid_person > n:
                break 

        if mid_person < n: #심사해야하는 인원수보다 적다면
            left = mid + 1
        else: #심사해야하는 인원수보다 많거나 같다면
            answer = mid #일단 저장해두고 계속 탐색
            right = mid - 1 
    return answer
        
