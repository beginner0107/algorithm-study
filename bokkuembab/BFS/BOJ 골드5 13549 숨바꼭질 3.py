from collections import deque

now, dest = map(int, input().split())

# 큐 선언 (현재 위치의 값으로 초기화)
q = deque([now])
# 소요 시간 저장 리스트 (걸리는 시간 최대로 초기화)
sec = [200000] * (100000 + 1)
sec[now] = 0    # 시작 위치의 시간 0으로 초기화

# 큐가 빌 때까지 확인
while q:
    # 큐에서 값 꺼내기
    loc = q.popleft()
    
    # 목표 위치에 도달했다면, 소요시간 출력 후 종료
    if loc == dest:
        print(sec[loc])
        break
    
    # 이동가능한 경우의 수 순회
    for move in [loc - 1, loc + 1, loc * 2]:
        if move < 0 or move > 100000:    # 범위를 넘어간다면, 무시
            continue
        
        # 순간이동일 때, 왼쪽에 입력 -> 더 높은 우선순위를 갖기 위함
        # (가중치가 0, 즉 시간 추가 없이 이동 가능하므로 )
        if move == loc * 2:
            if sec[loc] < sec[move]:    # 이동하는 것이 더 적게 걸린다면,
                q.appendleft(move)
                sec[move] = sec[loc]
        else:    # 순간이동이 아닐 때, 오른쪽에 입력   
            if sec[loc] + 1 < sec[move]:
                q.append(move)
                sec[move] = sec[loc] + 1