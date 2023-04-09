from collections import deque

def solution(begin, target, words):
    ans = 0
    
    q = deque()
    q.append([begin, 0])
    V = [0 for i in range(len(words))]
    
    while q:
        cur_word, cnt = q.popleft()
        if cur_word == target:
            ans = cnt
            break        
        
        for i in range(len(words)):
            temp_cnt = 0
            
            # 방문하지 않은 경우,
            if not V[i]:
                # 자리별로 비교
                for j in range(len(cur_word)):
                    if cur_word[j] != words[i][j]:
                        temp_cnt += 1
                # 딱 한 자리만 다르면 q에 추가
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    V[i] = 1
    return ans