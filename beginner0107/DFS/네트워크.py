def solution(n, computers):
    answer = 0
    li = []
    networks = [-1] * n  # 각 컴퓨터가 속한 네트워크의 번호를 저장할 리스트
    
    for i in range(n):
        li.append([])
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1:
                li[i].append(j)
    print(li)
    for i in range(n):
        if networks[i] == -1:
            answer += 1
            dfs(i, li, networks, answer)
    
    return answer

def dfs(node, li, networks, network_num):
    networks[node] = network_num
    
    for neighbor in li[node]:
        if networks[neighbor] == -1:
            dfs(neighbor, li, networks, network_num)
