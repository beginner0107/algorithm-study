import sys, heapq
input = sys.stdin.readline

# 입력 받기
v, e = map(int, input().split())    # v: 노드의 수, e: 간선의 수
start = int(input())    # 시작 노드
graph = [[] for _ in range(v + 1)]    # 노드 정보 저장 리스트
for _ in range(e):
    s, e, c = map(int, input().split())    # s에서 e로 가는 가중치가 c임
    graph[s].append((e, c))
    
# 모든 노드로의 최단거리를 무한대로 설정
INF = int(1e9)    # 무한대
distance = [INF] * (v + 1)

# 최단거리 계산
q = []    # 가장 비용이 적은 노드를 출력하기 위한 최소힙
heapq.heappush(q, (0, start))    # start 노드부터 q에 넣어줌 (비용, 노드) 순서대로
distance[start] = 0    # start에서 자신으로의 거리는 0임

while q:    # q가 비어있지 않은 동안 반복
    dist, now = heapq.heappop(q)    # q에서 값 꺼내기
    if distance[now] < dist:    # 이미 방문처리 했던 곳이면, 넘어가기
        continue
    
    for n, c in graph[now]:
        cost = dist + c    # 현재 노드를 거쳐가는 비용 계산
        if cost < distance[n]:    # 거쳐가는 비용이 더 적다면,
            distance[n] = cost    # distance 테이블 갱신,
            heapq.heappush(q, (cost, n))    # q에 넣어주기
       
# 계산한 최단거리 출력
for i in range(1, v + 1):
    if distance[i] == INF:    # 도달할 수 없다면, INF 출력
        print('INF')
    else:
        print(distance[i])