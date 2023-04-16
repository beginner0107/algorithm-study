def solution(jobs):
    #0,3 2,6 1,9
    #3+(0)-0 6+(3)-2 9+(9)-1
    #(tasktime) + (이전 tasktime합 = flag) - (작업 요청 시간)
    
    answer, flag = 0, 0 #flag : 현재까지의 작업 시간
    length = len(jobs)
    
    jobs.sort(key = lambda x:x[1])
    
    while jobs:
        temp = 0
        for i in range(len(jobs)):
            #아직 작업 요청 시점 이전일 수 있으므로 확인
            if jobs[i][0] <= flag : 
                flag += jobs[i][1]
                answer += flag - jobs[i][0]
                jobs.pop(i)
                temp = 1
                break
        #아직 작업 요청 시점 이전이라면 (break가 되지 않았으면)
        if temp == 0:
            flag += 1
    
    '''
    # 틀렸던 답
    from collections import deque
    jobs = deque(jobs)
    
    while jobs:
        start, tasktime = jobs.popleft()
        flag += tasktime
        answer +=  flag - start 
    '''  
    return answer // length