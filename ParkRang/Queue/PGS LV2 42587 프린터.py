from collections import deque
def solution(priorities, location):
    # 숫자 인덱스 배열 생성
    num = []
    for i in range(len(priorities)) :
        num.append(i)
    num = deque(num) # 숫자 인덱스 배열
    q = deque(priorities) # 중요도 배열

    cnt = 0
    
    while location in num :
        # 제일 왼쪽 값이 제일 크면 출력, 연관된 인덱스도 출력
        if q[0] == max(q) :
            q.popleft()
            num.popleft()
            cnt = cnt + 1
        # 아니라면 마지막으로 이동, 연관된 인덱스도 이동
        else :
            q.append(q.popleft())
            num.append(num.popleft())
        # 원하는 인덱스가 제출되면 종료되므로 카운트는 답이 됨.
        
    answer = cnt
    return answer
