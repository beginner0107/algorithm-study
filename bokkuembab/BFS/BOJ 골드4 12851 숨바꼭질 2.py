from collections import deque

# now: 현재 위치, dest: 목표 위치
now, target = map(int, input().split())

dist = [10 ** 6] * (10 ** 5 + 1)    # 이동하는 데 걸리는 최소 횟수 저장
q = deque([(now, 0)])    # 시작 위치 q에 넣어주기
dist[now] = 0    # 시작위치의 이동 횟수는 0으로 초기화
res = 0

while q:
    loc, cnt = q.popleft()
    
    if loc == target:    # 목표 위치에 도달한 경우 추가
        res += 1
    
    for id in [loc * 2, loc - 1, loc + 1]:    # 3가지 이동 경우 수행
        if 0 <= id <= 10 ** 5:    # 범위를 넘어가지 않고, 
            # 해당 위치로 이동한 최소 횟수인 경우, (처음 도달뿐만 아니라, 최소 도달을 찾으므로 같을 때도 추가)
            if cnt + 1 <= dist[id]:    
                dist[id] = cnt + 1    # dist 테이블 갱신,
                q.append((id, cnt + 1))    # q에 넣어주기

print(dist[target])            
print(res)