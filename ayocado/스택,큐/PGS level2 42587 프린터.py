"""
● 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42587

    일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 
    이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.
    
    1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
    2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
    3. 그렇지 않으면 J를 인쇄합니다.
    
    현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
    내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.
    
    - 입출력 예시
    
    priorities           location    return
    [2, 1, 3, 2]         2           1
    [1, 1, 9, 1, 1, 1]   0           5
    
● 생각
    deque를 이용
    1. 모든 문서의 위치에 대한 리스트 locations 생성
    2. max(priorities)가 맨 앞에 올 때까지 rotate(-1)
    3. max(priorities)를 popleft 로 제거 + 제거할 때마다 count에 1 더하기
    4. 제거한 원소가 location 값을 가지면, return count
    
    deque 모듈 쓰는게 시간복잡도면에서 좋은건지?
"""
from collections import deque

def solution(priorities, location):
    
    locations = []
    count = 1
    for i in range(len(priorities)):
        locations.append(i)
    
    priorities = deque(priorities)
    locations = deque(locations)
    
    while True:
        while priorities[0] != max(priorities):
            priorities.rotate(-1)
            locations.rotate(-1)
    
        if locations[0] == location:
            return count
        else:
            priorities.popleft()
            locations.popleft()
            count += 1

"""
● any를 사용한 풀이
    
    - any : 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수
    - all : 인자로 받은 반복 가능한 자료형(iterable)의 모든 요소가 참(True)이면 참(True)을 반환하는 함수
"""
def solution(priorities, location):
    
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
"""
● 나중에 확인할 풀이
"""
def solution(priorities, location):
    
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
        
    return answer