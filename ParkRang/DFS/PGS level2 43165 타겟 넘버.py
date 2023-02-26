# 갯수
answer= 0
def dfs(total, numbers,target, s) :
    global answer
    # 1. 종료 조건
    if len(numbers) == s :      # 마지막 숫자에 도달
        if total == target :    # 타겟 넘버와 같다면
            answer = answer + 1
        return;
    # 2. 수행 동작
    dfs(total-numbers[s], numbers,target, s+1)  # 값을 더함
    dfs(total+numbers[s], numbers,target, s+1)  # 값을 뺌
    
def solution(numbers, target):
    
    dfs(0, numbers,target, 0) # dfs 호출
    print(answer)   # 확인용
    return answer

