'''
UnboundLocalError: local variable 'answer' referenced before assignment
: 함수 내에서 변수를 참조할 때 해당 변수가 함수 내에서 할당되기 전에 참조되어서 발생하는 오류.
  => 
  
global   : 일반 함수 내에서 전역 변수를 사용할 때 사용 
noncocal : 중첩 함수 내에서 상위 함수의 변수를 사용할 때 사용
'''



def solution(begin, target, words):
    
    def dfs(begin, target, count):
        nonlocal answer
        
        if begin == target:
            answer = min(answer, count)
            return
        
        for i in range(len(words)):
            diff = 0
            # bigin과 words[i]를 한 글자씩 비교하여 몇 개가 틀린지 확인
            for j in range(len(begin)):
                if begin[j] != words[i][j]:
                    diff += 1
            
            # 위에서 확인한 틀린 개수가 1개 이고, 방문한적 없는 word이면
            if diff == 1 and visit[i] == False:
                visit[i] = True
                dfs(words[i], target, count+1)
                visit[i] = False
                
    
    answer = float('inf')
    arr = []
    visit = [False] * len(words)
    
    # words 리스트 안에 target이 있어야 begin -> target 변환 가능하므로
    # words 리스트 안에 target이 없으면 0 반환
    if target not in words:
        return 0
        
    dfs(begin, target, 0)
    
    return answer