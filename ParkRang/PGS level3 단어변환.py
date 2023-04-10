def solution(begin, target, words):
    # visited 배열 생성
    visited = [False] * len(words)
    answer = 0
    
    # dfs 
    def dfs(begin, target, words, cnt):
        nonlocal answer
        # 1. 종료 조건
        if begin == target:
            answer = cnt
            return
        # 2. 수행 동작
        for i in range(len(words)):
            if visited[i]:
                continue
        # begin이 단어들과 같다면 visited에 True, DFS
            k = 0
            for j in range(len(begin)):
                if begin[j] == words[i][j]:
                    k = k + 1
            if k == len(begin)-1:
                visited[i] = True
                dfs(words[i], target, words, cnt + 1)
                visited[i] = False

    dfs(begin, target, words, 0)
    return answer
