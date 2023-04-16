from collections import deque

def solution(progresses, speeds):
    answer = []
    
    # 기능들의 남은 개발 일 큐
    days = deque([(100-p) // s+((100 - p) % s > 0) for p, s in zip(progresses, speeds)])
    
    while days :
        cnt = 1 # 배포할 기능
        cur = days.popleft() # 가장 앞의 기능의 남은 개발일 수
        while days and days[0] <= cur : # 현재 기능보다 남은 개발 일수가 적거나 같은 기능
            cnt = cnt + 1
            days.popleft()
        answer.append(cnt)
        
    return answer
