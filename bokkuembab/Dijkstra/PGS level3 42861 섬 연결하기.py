# 크루스칼 알고리즘

# 부모 노드가 같은지 확인하는 함수
def find_parent(parent, x):
    
    if parent[x] == x:  # 부모노드에 도달하면 값 반환
        return parent[x]
    
    return find_parent(parent, parent[x])

# 부모 노드를 합치는 함수
def union_parent(parent, a, b):
    
    # 각 노드의 부모 노드 확인 및 이동
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    
    # 부모 노드가 더 작은 수로 변경
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

def solution(n, costs):
    
    ans = 0  # 최소 비용
    # 부모 노드 저장 리스트: 자기 자신으로 모든 노드의 부모 노드 설정
    parent = [i for i in range(n)]
    
    # 비용이 적은 간선 기준으로 오름차순 정렬
    costs = sorted(costs, key=lambda x: x[2])
    
    # 노드를 하나씩 확인하며 섬 연결하기
    for edge in costs:
        
        s, e, c = edge   # 노드1, 노드2, 비용
        
        # 사이클이 발생하지 않는 경우에만 연결해주기
        if find_parent(parent, s) != find_parent(parent, e):
            union_parent(parent, s, e)   # 부모노드 합침
            ans += c  # 비용 추가
    
    return ans