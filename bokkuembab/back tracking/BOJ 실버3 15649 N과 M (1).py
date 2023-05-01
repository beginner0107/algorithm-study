# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 사전 순으로 증가하는 순서로 출력

n, m = map(int, input().split())

stack = []    # 지나온 경로를 저장할 스택

# 1부터 시작해서 m개만큼 중복없이 뽑아야 함
def backtracking():
    if len(stack) == m:    # 종료 조건 
        print(' '.join(map(str, stack)))
        return 
    
    for i in range(1, n + 1):
        
        if i not in stack:    # 방문한 적 없다면,
            stack.append(i)
            backtracking()
            stack.pop()
            
backtracking()