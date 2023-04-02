def solution(tickets):
    # 1. 출발지별로 도착지 정보를 담고있는 딕셔너리 생성
    routes = {}
    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    
    # 2. 도착지를 역순으로 정렬 
    # 알파벳이 뒤인 것부터 pop하기 위해
    for route in routes:
        routes[route].sort(reverse=True)
    
    # 3. DFS
    q = ["ICN"]
    ans = []
    while q:
        flight = q[-1]
        if flight not in routes or len(routes[flight]) == 0:
            ans.append(q.pop())
        else:
            q.append(routes[flight].pop())
    
    # 경로를 뒤집어서 알파벳 순서가 앞서는 경로 찾기
    return ans[::-1]