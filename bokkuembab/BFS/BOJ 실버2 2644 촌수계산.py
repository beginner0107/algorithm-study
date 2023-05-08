# 촌수 계산
# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산

import sys
input = sys.stdin.readline
from collections import deque

total = int(input())    # 전체 사람의 수
t1, t2 = map(int, input().split())    # 촌수 계산할 두 사람
m = int(input())    # 부모 자식들의 관계 계수
graph = [[] for _ in range(total + 1)]    # 부모 자식 관계 (부모, 자식)
for _ in range(m):    # 부모 자식 관계 입력
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

# 부모 자식 관계는 연결된 노드의 정보이며, t1과 t2의 촌수는 t1에서 t2로 가는 최단 경로와 같음
# 노드 간의 거리 정보가 없으므로 bfs로 풀이 가능
visited = [False] * (total + 1)    # 방문 여무 리스트
q = deque([(t1, 0)])    # 시작 노드 초기화
ans = -1    # 촌수 초기화

while q:
    now, cnt = q.popleft()
    
    for p in graph[now]:    # 연결된 모든 노드 탐색
        
        if p == t2:    # 목표 t2에 도달했으면,
            ans = cnt + 1    # 최종 촌수 (t2로 이동 횟수 1 추가)
            break
        
        if not visited[p]:    # 방문하지 않았으면,
            q.append((p, cnt + 1))    # 촌수 추가하고 q에 넣어주기
            visited[p] = True    # 방문처리
            
print(ans)    # 결과 출력