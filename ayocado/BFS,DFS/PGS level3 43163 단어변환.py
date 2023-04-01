def solution(begin, target, words):
    from collections import deque

    # BFS를 위해 큐 생성
    queue = deque()
    visited = [0] * len(words)
    length = len(begin)

    # 조건에 맞는 단어 push : [단어, step] 형태
    # push한 단어는 방문 입력
    for word in words:
        same = 0
        for i in range(length):
            if begin[i] == word[i]:
                same += 1
        if same == length - 1:
            queue.append([word, 1])
            visited[words.index(word)] = 1

    # BFS 진행
    while queue:
        word, step = queue.popleft()

        # target 단어일 경우 step 출력하고 중지
        if word == target:
            return step
        # 방문하지 않은 단어 중, 조건 맞으면 push : [다음 단어, step + 1]
        # push한 단어는 방문 입력
        for i in words:
            same = 0
            if visited[words.index(i)] != 1:
                for j in range(length):
                    if word[j] == i[j]:
                        same += 1
                if same == length - 1:
                    queue.append([i, step + 1])
                    visited[words.index(i)] = 1
    # target을 찾지 못하고 끝난 경우 0 출력
    return 0