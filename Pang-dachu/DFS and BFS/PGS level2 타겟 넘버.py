# [생각]
# 하나의 숫자에 대해서 [더하기, 빼기] 두가지 경우를 고려하면서 
# 트리처럼 뻗어나가는 건가 ?

# 하나의 숫자에 대해서 경우의수를 같이 생각하는 거니까 BFS? 

# 근데.. 만들어져있는게 아니라 만들어 나가는 건데 어떻게 하지 ?
# 큐에 있는거 다 빼서 한번에 계산하고 다 넣어버리나 ? 맞는듯 

from collections import deque 

def solution(numbers, target) :
    
    q = deque()
    # 시작은 0부터 
    q.append( 0 )
    
    # flag를 넣어 한번 사이클을 체크
    q.append( "flag" )
    
    for i in numbers :
        while q :
            x= q.popleft()
            
            if x == "flag" :
                q.append("flag")
                break
            q.append( x + i )
            q.append( x - i )

    return q.count(target)