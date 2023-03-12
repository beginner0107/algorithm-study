# 위치와 목표 입력
N,K = list(map(int, input().split()))

# 큐 생성 / 최대값 생성 / visited 배열 생성
q = []
MAX = 100001
visited = [0] * (MAX)

# BFS 함수 생성
def BFS(q, N, K) :
    # 첫값 추가
    q.append([N,0])

    # 배열이 0이 아니라면 q의 첫 값을 가져와서 현재 위치, 시간으로 저장
    while len(q) > 0 :
        data = q.pop(0)
        current = data[0]
        count = data[1]
        visited[current] = 1 # 방문한 위치 표시

        if current == K :   # 도달하면 종료
            return count

        # 2배로 커질 수 있고 그 위치에 도달하지 않았다면 첫 값으로 저장
        if current * 2<=MAX and not visited[current*2] :
            q.insert(0, [current*2, count])
        # 목표보다 작고 최대값보다 작고 도달하지 않은 위치라면 값에 추가
        if current < K and current < MAX and not visited[current+1] :
            q.append([current+1, count +1])
        # 목표가 0보다 크고 그 위치에 도달하지 않았다면 값에 추가
        if current > 0 and not visited[current-1] :
            q.append([current-1, count+1])

# 함수를 통해 답 생성
print(BFS(q, N, K))
