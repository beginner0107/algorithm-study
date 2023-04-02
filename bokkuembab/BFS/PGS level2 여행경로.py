def solution(tickets):
    air = dict()    # 항공권 정보 저장
    for s, e in tickets:
        if s not in air:
            air[s] = [e]
        else:
            air[s].append(e)
    
    # 여행 경로 내림차순 정렬
    for a in air:
        air[a].sort(reverse=True)
    
    start = 'ICN'
    stack = [start]
    ans = []
    
    while stack:    # 모든 노드 순회
        srt = stack[-1]    # 가장 위에 있는 데이터
        
        if srt not in air or not air[srt]:    # 해당 공항에서 출발하는 경로가 없거나, 방문하지 않은 경로가 없다면,
            ans.append(stack.pop())
        else:
            stack.append(air[srt].pop())    # 마지막 여행 경로를 스택에 저장
            

    return ans[::-1]    # 거꾸로 저장돼 있으므로 거꾸로 출력