import sys, heapq
input = sys.stdin.readline

# 입력 받기
city_n = int(input())    # 도시(노드)의 수
bus_n = int(input())    # 버스(간선)의 수
graph = [[] for _ in range(city_n + 1)]
for _ in range(bus_n):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, target = map(int, input().split())    # 출발 도시, 목표 도시

# 초기값 설정
INF = int(1e9)    # 무한대 값 설정
distance = [INF] * (city_n + 1)    # 각 도시까지의 최단 거리 무한대로 설정

# 최단거리 계산
q = []    # 최단 거리 기준으로 노드들 저장할 큐
heapq.heappush(q, (0, start))    # 시작 도시 큐에 넣기 (첫번째 요소 기준으로 정렬되므로 비용 먼저 넣기)
distance[start] = 0    # 시작 도시의 최단거리 distance에 넣어주기 (자기 자신으로의 최단 거리는 0)

while q:    # 큐가 빌 때까지 탐색
    cost, city = heapq.heappop(q)    # 큐에서 값 꺼내기
    if distance[city] < cost:    # 방문했던 도시면, 넘어가기
        continue
    
    # 인접 노드들 방문하며 확인
    for n, c in graph[city]:
        total = cost + c
        if total < distance[n]:    # 현재 도시를 경유하는 것이 더 적은 비용이 든다면,
            distance[n] = total    # distance 테이블 갱신,
            heapq.heappush(q, (total, n))    # 큐에 넣어주기
            
print(distance[target])    # 출발도시에서 목표도시까지의 최단거리 출력