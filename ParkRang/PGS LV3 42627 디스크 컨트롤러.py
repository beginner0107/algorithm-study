jobs = [[0,5],[1,2],[5,5]]#[[0,3],[0,4],[2,6],[3,2], [7,4], [2,9],[11,5]]

def solution(jobs):
    answer = 0
    time, work, waitingTime = 0, 0, 0 #현재 시간, 일이 남은 시간, 대기 시간
    waiting = [] # 작업 대기열 배열
    l = len(jobs)
    #jobs.sort() 하면 안됨(처음에 입력한 값 먼저 들어가야 하기 때문에)
    onWork = True
    
    # 작동 시작
    while onWork :
        MIN = 10000 # 최소값 생성
        mdx = 0 # 최소값 인덱스
        
        # 대기열의 대기시간 + 1
        for i in range(len(waiting)) :
            waiting[i][2] = waiting[i][2] + 1

        # 작업 배열에서 요청시간에 맞는 작업을 대기열로 이동
        # for i in range() 쓰면 안됨
        e = 0
        while e < len(jobs) :
            if jobs[e][0] <= time :
                jobs[e].append(0)
                waiting.append(jobs.pop(e))
            else :
                e = e + 1

        # 작업 대기열에 2개 이상 있을 경우, 먼저 끝나는 것부터 우선순위로 지정
        if len(waiting)>=2:
            for i in range(len(waiting)) :
                if MIN > waiting[i][1] :
                    MIN = waiting[i][1]
                    mdx = i

        # 작업 진행 중일 경우 작업시간 1 소요
        if work > 0 :
            work = work - 1
            
        # 작업이 끝났고 작업 대기열이 있을 경우
        # 다음 작업을 인덱스에 따라 처리
        if work == 0 and len(waiting) > 0:
            work = work + waiting[mdx][1]
            waitingTime = waitingTime + waiting[mdx][1] + waiting[mdx][2]
            #print('waitingTime에', waiting[mdx][1] + waiting[mdx][2], '추가')
            waiting.pop(mdx)

        #print(time, work, jobs, waiting)
        
        # 시간 증가
        time = time + 1
        # 종료조건
        if work == 0 and len(jobs)== 0:
            onWork = False

    answer = waitingTime / l
    return int(answer)

print(sol(jobs))
