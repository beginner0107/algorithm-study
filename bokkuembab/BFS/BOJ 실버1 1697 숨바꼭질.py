from collections import deque

def bfs(node, target):
    # 큐 선언 및 처음 위치 방문 처리
    q = deque([node]) 
    # 트리의 깊이 저장 리스트 초기화 (걸린 시간 최대로 초기화)
    sec = [1000000] * (200000 + 1)
    sec[node] = 0    # 첫번째 위치의 시간 0으로 초기화
    
    # 큐가 비어있지 않은 동안 반복
    while q:
        now = q.popleft()    # 큐에서 값 꺼내기
        
        # 목표 위치에 도달했으면, 걸린 시간 출력
        if now == target:
            return sec[now]
        
        # 이동 경우의 수 확인
        for move in [now + 1, now - 1, now * 2]:
            if (move >= 0 and move < 200000) and (sec[now] + 1 < sec[move]):    # 위치가 범위에 있고, 전보다 적게 걸리는 경우에만 방문
                q.append(move)
                sec[move] = sec[now] + 1
                
# now: 현재 위치, target: 도착할 위치
now, target = map(int, input().split())    

print(bfs(now, target))