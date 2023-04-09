def solution(tickets):
    # 딕셔너리로 변경하기 전, 내림차순 정렬
    tickets.sort(reverse=True)

    # 딕셔너리 생성 -> key : 출발지, value : 도착지
    ticketsDict = {}
    for i in range(len(tickets)):
        if tickets[i][0] not in list(ticketsDict.keys()):
            ticketsDict[tickets[i][0]] = [tickets[i][1]]
        else:
            ticketsDict[tickets[i][0]].append(tickets[i][1])

    # DFS
    # 최근 도착지를 출발지로 설정 > 대응하는 도착지를 stack에 push
    # 만약 대응하는 도착지가 없으면 stack.pop()을 answer로 push
    # DFS 완료 후, answer를 reverse
    stack = ['ICN']
    answer = []
    while stack:
        now = stack[-1]
        if now not in list(ticketsDict.keys()) or not len(ticketsDict[now]):
            answer.append(stack.pop())
        else:
            stack.append(ticketsDict[now].pop())
    return answer[::-1]