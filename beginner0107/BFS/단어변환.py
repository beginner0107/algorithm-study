from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)

    q = deque([(begin, 0)])  # 괄호로 묶어서 튜플로 넣어줌
    while q:
        ch, count = q.popleft() # 시작 단어, 변환 횟수
        diff_count = 0

        for i in range(len(ch)):
            if ch[i] != target[i]:
                diff_count += 1 # 단어와 타겟 단어가 다르면 1증가

        if diff_count == 1: # 만약 다른게 하나라면! 무조건 찾을 수 있음
            return count + 1

        for i in range(len(words)): # words를 반복문 돌림
            diff_count = 0
            for j in range(len(words[i])):  # 기존 단어(ch)와 비교해서 다른 단어가 하나여야 함
                if ch[j] != words[i][j]:
                    diff_count += 1
            if diff_count == 1 and not visited[i]: # 다른 단어가 하나이고 방문하지 않았을 경우
                visited[i] = True
                q.append((words[i], count + 1)) # 큐에 넣어준다

    return 0
