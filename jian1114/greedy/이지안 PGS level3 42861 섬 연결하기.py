'''
[크루스칼 알고리즘]
싸이클 형성하는지만 확인 
'''

def solution(n, costs):
    answer = 0
    # 1. 비용이 적은 순으로 정렬
    costs.sort(key = lambda x: x[2])
    
    # 2. 연결된 섬
    connect = set([costs[0][0]])
    
    # 3. 다 연결될 때까지
    while len(connect) != n:
        for v in costs:
            island1 = v[0]
            island2 = v[1]
            cost = v[2]
    
            # 3-1. 둘 다 이미 연결되었다면 pass
            if island1 in connect and island2 in connect:
                continue
                
            # 3-2. 둘 중 하나만 연결 -> 섬 추가 & 비용 +
            if island1 in connect or island2 in connect:
                connect.update([island1, island2])
                answer += cost
                break
    
    return answer