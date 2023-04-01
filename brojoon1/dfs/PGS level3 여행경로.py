def solution(tickets):
    answer = []
    visit = [False] * len(tickets)
    
    def dfs(depth, now, string):
        # tickets 리스트를 다 돌면 answer에 string 담고 return
        if depth == len(tickets):
            answer.append(string)
            return
        
        for idx, ticket in enumerate(tickets):
            if visit[idx] == False and now == ticket[0]:
                visit[idx] = True
                dfs(depth+1, ticket[1], string+[ticket[1]])
                visit[idx] = False
    
    dfs(0, 'ICN', ['ICN'])
    
    answer.sort()
    
    return answer[0]