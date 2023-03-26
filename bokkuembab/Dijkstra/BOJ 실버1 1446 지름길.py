# 모든 지름길의 노드를 저장
# -> 모든 지름길까지 가는 데 걸리는 거리로 초기화
# -> 노드들을 순회하며 최단 거리 갱신해주기
import sys, heapq
input = sys.stdin.readline

# 입력 받기
nums, target = map(int, input().split())    # 지름길의 개수, 고속도로의 길이
graph = {target: [], 0: []}    # 지름길의 연결 정보
nodes = {target, 0}    # 노드를 저장할 집합

for _ in range(nums):
    s, e, c = map(int, input().split())
    if e > target:    # 지름길의 도착지가 목표위치보다 크면 무시
        continue
    
    if s in graph:
        graph[s].append((e, c))
    else:
        graph[s] = [(e, c)]
    
    nodes.add(s)
    nodes.add(e)

# nodes 정렬
nodes = sorted(nodes)

# 최단 거리 테이블 최대값으로 초기화
# 지름길 노드들을 모두 연결해 주기
distance = dict()
for i, n in enumerate(nodes):
    distance[n] = int(1e9)
    if i < len(nodes) - 1:
        next_node = nodes[i + 1]
    else:
        next_node = target
        
    if n in graph:
        graph[n].append((next_node, next_node - n))
    else:
        graph[n] = [(next_node, next_node - n)]

# 작은 것부터 시작해야 하므로 graph의 key 순서대로 정렬
graph = dict(sorted(graph.items(), key=lambda x: x[0]))

# 다익스트라 구현
def dijkstra(start):
    # 지름길의 첫번째 요소를 시작 노드로 설정, 비용을 큐에 넣어주기
    q = []    # 최소 거리를 확인하기 위해 선언
    heapq.heappush(q, (0, start))    # 최소힙은 첫번째 요소순으로 정렬되므로 (비용, 노드) 순으로 넣기
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)    # 가장 비용이 적은 노드가 출력됨
        if distance[now] < dist:    # 처리된 적 있다면, 넘기기
            continue
        
        for n, c in graph[now]:
            cost = dist + c
            if cost < distance[n]:    # 현재 노드를 거쳐 인접 노드들에 도착하는 것이 최단 거리면
                distance[n] = cost    # distance 테이블 갱신
                heapq.heappush(q, (cost, n))    # q에 넣어주기

dijkstra(0)

print(distance[target])