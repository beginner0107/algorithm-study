from collections import deque

def solution(tickets):
    graph = {}
    for start, end in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    
    for key in graph:
        graph[key].sort(reverse=True)
    
    stack = ["ICN"]
    answer = []
    while stack:
        node = stack[-1]
        if node not in graph or not graph[node]:
            answer.append(stack.pop())
        else:
            stack.append(graph[node].pop())

    return answer[::-1]
