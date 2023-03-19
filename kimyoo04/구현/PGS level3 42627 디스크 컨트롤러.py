# https://school.programmers.co.kr/learn/courses/30/lessons/42627

'''
핵심
1. ((작업이 기다리는 시간 + 작업시간)의 합 / 모든 작업 수) 를 최소화
2. 현재 처리 가능한 요청 중에 가장 짧은 작업시간을 우선 처리 (최소힙) -> 기다리는 시간 최소화
3. jobs를 요청 시간 순으로 정렬 -> 시작한 작업의 걸리는 시간 - 요청시간 > 0 -> 힙에 삽입
4. 작업이 끝나면 -> 힙의 heappop으로 작업 시작
5. 반복

필요한 변수
- waiting = []  <- 진행중인 작업 외 나머지 작업 중에 기달리는 작업
- start, now = -1, 0 <- 기달리는 작업을 찾기위한 범위
- total = 0  <- 각 작업별 요청부터 종료까지 소요시간
'''
from heapq import heappush, heappop


def solution1(jobs):
    cnt_jobs = len(jobs)
    total = 0 # 종합시간
    start, now = -1, 0 # 현재작업 시작시간, 작업이 끝난 현재 시간
    i = 0 # 작업 카운트
    waiting = [] # 대기 중인 작업 (최소힙)

    while i < cnt_jobs:
        for job_start, job_time in jobs:
            # 실행한 작업보다 일찍 혹은 같게 작업요청이 들어왔을때
            if start < job_start <= now:
                heappush(waiting, (job_time, job_start)) # 작업시간을 기준으로 최소힙 생성

        if waiting:
            ongoing_time, ongoing_start = heappop(waiting)
            # 작업의 시작시간
            start = now
            # 작업시간을 더한 것이 현재시간
            now += ongoing_time
            # 현재시간 - 작업의 시작시간을 축적
            total += now - ongoing_start
            i += 1
        else:
            now += 1 # 현재 실행할 작업이 없을 때 1ms 더하기

    return int(total / cnt_jobs)


import heapq

def solution2(jobs):
    tasks = sorted([(x[1], x[0]) for x in jobs],
                    key=lambda x: (x[1], x[0]),
                    reverse=True)
    waiting = []
    heapq.heappush(waiting, tasks.pop())
    now, total = 0, 0

    while waiting:
        duration, req_time = heapq.heappop(waiting)
        now = max(now + duration, req_time + duration)
        total += now - req_time

        while len(tasks) > 0 and tasks[-1][1] <= now:
            heapq.heappush(waiting, tasks.pop())

        if len(tasks) > 0 and len(waiting) == 0:
            heapq.heappush(waiting, tasks.pop())

    return total // len(jobs)

a = solution2([[0, 3], [1, 9], [2, 6]])
print(a)
