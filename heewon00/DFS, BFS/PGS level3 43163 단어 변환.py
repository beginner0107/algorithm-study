from collections import deque
def solution(begin, target, words):
    if target not in words: #target이 word list에 없다면
        return 0
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        cnt = dict({start:0}) #변환 횟수 cnt
        while queue:
            v = queue.popleft()
            
            if v==target:
                return cnt[target]
            
            for word in words:
                # 이미 방문했다면 pass
                if word in cnt.keys(): continue 
                
                # 아직 방문하지 않았다면
                diff = 0
                for i in range(len(word)):
                    if word[i] != v[i]:
                        diff+=1
                if diff==1: # 하나만 다른 경우
                    cnt[word] = cnt[v]+1 
                    queue.append(word) 
        return 0 # 불가능한 경우
            
    return bfs(begin)
