from collections import deque

start, end = map(int, input().split())    # now: 현재 위치, target: 목표 위치

dist = [10 ** 6] * (10 ** 5 + 1)    # 최단거리는 최대값으로 초기화
path = [-100] * (10 ** 5 + 1)    # 경로를 저장할 리스트

# 시작 지점 초기화
q = deque([(start, 0)])
dist[start] = 0    # 현재 위치로의 이동 횟수는 0

while q:
    now, cnt = q.popleft()
    
    if now == end:
        break
    
    for move in [now * 2, now + 1, now - 1]:
        if 0 <= move <= 10 ** 5:    # 범위를 넘지 않고,
            if cnt + 1 < dist[move]:    # 최단 횟수라면,
                dist[move] = cnt + 1    # dist 테이블 갱신하고,
                q.append((move, cnt + 1))    # q에 넣어주고,
                path[move] = now    # path 테이블에 경로 추가하기
                
print(dist[end])     # 최단 이동 횟수 출력

# 경로 타고 넣어주기
i = end
res = []
while i != start:
    res.append(i)
    i = path[i]
res.append(start)
print(*res[::-1])    # 경로 거꾸로 출력