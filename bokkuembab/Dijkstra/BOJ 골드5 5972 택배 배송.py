import sys, heapq
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())    # n: 노드 수, m: 간선 수
graph = [[] for _ in range(n + 1)]    # 노드 연결 정보 저장 리스트
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))
  
# 초기값 설정
INF = int(1e9)    # 무한값으로 설정
distance = [INF] * (n + 1)    # 모든 노드의 최단거리를 무한값으로 설정
    
# 다익스트라 구현
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))    # 첫번째 요소의 값 순서대로 정렬되므로, (비용, 노드) 순서대로 넣기
    distance[start] = 0    # 처음 자기 자신으로의 비용은 0으로 갱신
    
    while q:    # 큐가 빌 때까지 반복
        dist, now = heapq.heappop(q)    # 값 꺼내기
        if distance[now] < dist:    # distance 테이블의 값과 비교해, 이미 처리한 노드이면 넘어가기
            continue
        
        # 인접 노드들 모두 방문하며 확인
        for n, c in graph[now]:
            cost = dist + c
            if cost < distance[n]:    # 현재 노드를 거쳐 가는 것이 더 적은 비용이 든다면,
                heapq.heappush(q, (cost, n))    # 큐에 넣어주고,
                distance[n] = cost    # distance 테이블 갱신
    
# 다익스트라 알고리즘 수행
dijkstra(1)    # 시작 농부는 항상 1에 위치함

print(distance[n])    # 도착 농부는 항상 n에 위치함