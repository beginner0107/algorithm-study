from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n_com = int(input())    # 컴퓨터의 수
n_net = int(input())    # 컴퓨터끼리 연결된 네트워크의 수
coms = [[] for _ in range(n_com + 1)]    # 컴퓨터 간의 연결 정보 저장 리스트
for _ in range(n_net):
    s, e = map(int, input().split())
    coms[s].append(e)
    coms[e].append(s)
    
# 초기 값 설정
cnt = 0    # 시작 컴퓨터를 통해 감염되는 컴퓨터의 수
start = 1    # 시작 컴퓨터는 1
visited = [False] * (n_com + 1)    # 방문 여부 리스트
q = deque([start])
visited[start] = True    # 시작 컴퓨터 방문처리

while q:    # 큐가 빌 때까지 반복
    c = q.popleft()
    
    # 현재 컴퓨터와 연결된 컴퓨터 모두 확인
    for i in coms[c]:
        if not visited[i]:    # 방문한 적 없다면,
            visited[i] = True    # 방문처리,
            q.append(i)    # q에 추가,
            cnt += 1    # 감염 컴퓨터 늘려주기
            
print(cnt)    # 결과 출력