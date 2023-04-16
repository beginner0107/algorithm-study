from collections import deque
def solution(begin, target, words):
    
    ans = 0    # 변환 횟수
    visited = [False] * len(words)
    q = deque([(begin, ans)])    # 처음 시작 단어 q에 넣어주기
    
    while q:
        now, cnt = q.popleft()
        
        for idx, w in enumerate(words):
            
            if now == target:    # 목표한 단어에 도달하면,
                ans = cnt    # 변환 횟수 수정 후 반복 종료
                break
            
            if not visited[idx]:    # 방문하지 않았다면,
                tmp = len([i for i, j in zip(now, w) if i != j])    # 다른 글자의 수
                if tmp == 1:    # 글자가 하나만 다르다면,
                    q.append((w, cnt + 1))    # q에 넣어주기
                    visited[idx] = True    # 방문처리

    return ans