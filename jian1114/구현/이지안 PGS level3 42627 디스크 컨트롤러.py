def solution(jobs):
    ans, start, len_job = 0, 0, len(jobs)

    # '작업의 소요시간'이 짧은 것부터 시작
    jobs = sorted(jobs, key=lambda x: x[1])
    
    # 작업이 존재하면
    while len(jobs) != 0:
        for i in range(len(jobs)):
            # 작업 시점이 start 보다 큰 경우
            if jobs[i][0] <= start:
                start += jobs[i][1]
                ans += start - jobs[i][0]
                jobs.pop(i)
                break
            
            # 작업 시점 0초에 투입되는 시간이 없는 경우
            if i == len(jobs) - 1:
                start += 1

    return ans // len_job