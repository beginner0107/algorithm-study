def solution(tickets):
    answer = []
    visited = [0]*len(tickets)
    
    def dfs(start):
        answer.append(start)
        for i in range(len(tickets)):
            #출발 항공이 start와 같고 아직 사용하지 않은 티켓인 경우
            if tickets[i][0]==start and not visited[i]:
                visited[i]=1
                #현재 티켓의 도착 항공이 출발지인 티켓을 찾음
                dfs(tickets[i][1])

                # 모든 항공권을 사용한 경우
                if 0 not in visited : 
                    return answer
            
                # 아직 사용하지 않은 항공권이 남아있다면 해당 항공권은 나중에 사용해야 함
                else: 
                    visited[i]=0 ; answer.pop()
                
    #조건 - 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
    tickets.sort(key=lambda x: (x[0], x[1]))
    
    return dfs('ICN')
