'''
수행 시간이 짧은 작업부터 처리해야 요청시간+작업소요시간이 짧을 것임
'''

def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)

    # 소요시간 우선 정렬
    jobs = sorted(jobs, key=lambda x: x[1])

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 +1
            if i == len(jobs) - 1:
                start += 1

    return answer // length