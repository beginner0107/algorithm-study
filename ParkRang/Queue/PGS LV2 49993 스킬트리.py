from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    # skill_trees 하나씩 검사
    for i in skill_trees :
        s = deque(skill)
        
        # 스킬트리 한 단어씩 검사
        for j in i :
            # 스킬 목록에 없으면 넘어감
            if j not in skill :
                continue
            # 스킬 목록에 있는데 첫 번째 스킬트리가 아니면 X
            if j != s.popleft():
                break
        else :
            answer = answer + 1
    return answer
