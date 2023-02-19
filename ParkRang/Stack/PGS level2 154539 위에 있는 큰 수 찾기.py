def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 인덱스 스택
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]: # 스택이 0이 아니고 뒤에 큰 수가 있을 시
            idx = stack.pop()        # 현재 인덱스 다음 큰수를 현재 인덱스로 갱신
            answer[idx] = numbers[i]    #다음 큰 수 입력
        stack.append(i)
    return answer