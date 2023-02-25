"""
● 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

    프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

    또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

    먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 
    return 하도록 solution 함수를 완성하세요.

    - 입출력 예시
    progresses	               speeds	            return
    [93, 30, 55]	           [1, 30, 5]	        [2, 1]
    [95, 90, 99, 99, 80, 99]   [1, 1, 1, 1, 1, 1]	[1, 3, 2]
    
    
● 생각
    큐 문제
    deque 쓰려다가 실패
    시간 복잡도가 높은지?
    
    progresses에 speeds를 한번씩 더해주다가, 진도가 100에 다다르면 앞에서부터 진도 100 이상인 원소 개수 파악
    work_done : 완료한 작업 index
    count : 한번에 배포할 작업 개수
"""
def solution(progresses, speeds):
    
    work_done = 0
    release = []
    
    while work_done != len(progresses):
        progresses = list(map(lambda x,y:x+y, progresses, speeds))
        
        if progresses[work_done] >= 100:
            count = 0
            while progresses[work_done] >= 100:
                work_done += 1
                count += 1
                if work_done == len(progresses):
                    break
            release.append(count)
    
    return release

"""
● 다른 풀이
    ceil 사용 안하고 음수 나눗셈을 이용해서 올림
    ex) -(-5//2) = -(-3) = 3
"""
def solution(progresses, speeds):
    
    Q=[]
    
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
            
    return [q[1] for q in Q]
