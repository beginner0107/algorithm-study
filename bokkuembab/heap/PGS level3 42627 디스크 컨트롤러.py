# 기다리는 시간을 줄이려면, 작업 시간이 짧은 작업부터 하는 것이 이득
# 그렇지만, 먼저 들어온 것을 빠르게 처리하는 것도 중요
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리! -> 처음에 들어온 작업은 무조건 시작된다는 뜻!
# 힙에 값을 넣어주면, 자동으로 값이 작은 순서대로 정렬됨

# 테케 19번 안되는 문제 해결!

from heapq import heappush, heappop

def solution(jobs):
    
    times = 0    # 각 작업들의 요청~종료 시간의 합
    now = 0    # 현재시간
    tasks = []    # 힙 생성
    qjobs = sorted(jobs, reverse=True)    # 요청 시간 내림차순 정렬 (뒤에서부터 작은 것 제거할 예정 (스택))
    
    while qjobs or tasks:    # 작업이 모두 수행될 때까지 반복
        
        # 이전 작업이 끝나는 시간 기준, 요청된 작업들 불러오기
        while qjobs:
            if qjobs[-1][0] > now:
                break
            srt, l = qjobs.pop()  # jobs에서 제거
            heappush(tasks, (l, srt))  # (작업시간, 요청시간) 순서로 heap에 넣어주기
        
        # 작업시간이 가장 짧은 작업 수행
        if tasks:    # 기다리고 있는 작업이 있다면,
            l, srt = heappop(tasks)    # heap에서 첫번째 값 제거
            now += l    # 작업이 끝나는 시간으로 현재 시간 변경
            times += (now - srt)    # times에 시간 추가
        else:    # 기다리고 있는 작업이 없다면, 다음으로 제일 먼저 요청되는 작업 시작
            srt, l = qjobs.pop()  # jobs에서 첫번째 값 제거
            now = srt + l    # 새로운 작업이 끝나는 시간으로 현재 시간 변경
            times += l    # times에 시간 추가  
        
    return times // len(jobs)    # 평균 시간 출력