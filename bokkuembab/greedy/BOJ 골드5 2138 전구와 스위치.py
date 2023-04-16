# 전구와 스위치
# 0은 켜져 있는 상태, 1은 꺼져 있는 상태
# 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게
# 양쪽, 자기 자신만 바뀜
# 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 -> bfs


# 인터넷 확인 후 푼 풀이
# 처음부터 끝까지, 이전 전구의 상태에 따라 토글
import copy

n = int(input())    # 전구의 수
start = list(input())   # 현재 전구의 상태
target = list(input())    # 목표 전구의 상태


def is_toggle(now, target):
    now = copy.deepcopy(start)
    ans = 0    # 토글 횟수 초기화
    
    # 두번째 스위치부터 마지막까지 토글 여부 확인
    for i in range(1, n):
        
        if now == target:    # 목표 상태 도달하면, 종료
            return ans
        
        if now[i - 1] != target[i - 1]:    # 현재 위치의 왼쪽 스위치가 목표 상태와 같지 않으면,
            for s in range(i - 1, i + 2):    # 자기 자신과 양쪽 스위치 토글하고, 
                if s < n:    # 마지막 스위치를 위한 범위 제한
                    now[s] = '0' if now[s] == '1' else '1'
            ans += 1    # 횟수 1 늘려주기
            
    return ans if now == target else 1e9

# 두번째 스위치부터 누르는 경우
res = is_toggle(start, target)

# 첫번째 스위치를 눌러야 하는 경우
start[0] = '0' if start[0] == '1' else '1'
start[1] = '0' if start[1] == '1' else '1'

res = min(res, is_toggle(start, target) + 1)

if res < 1e9:
    print(res)
else:
    print(-1)

# # 메모리 초과 문제로 실패ㅠㅠ
# from collections import deque

# n = int(input())    # 전구의 수
# start = list(input())    # 현재 전구의 상태
# target = list(input())    # 목표 전구의 상태

# visited = [start]    # 시작 상태 넣어주기
# q = deque([(start, 0)])    # start의 현재 위치, 상태, 변경 횟수
# ans = -1    # 정답 횟수 초기화

# while q:
#     now, cnt = q.popleft()
    
#     if now == target:    # 목표 상태에 도달하면, 종료
#         ans = cnt
#         break
    
#     for i in range(n):    # i번째 스위치를 눌렀을 때,
#         rev = now.copy()
#         for ri in range(i - 1, i + 2):    # 양쪽과 자기 자신 방문
#             if 0 <= ri < n:    # 인덱스 범위를 넘어가지 않을 때만,
#                 rev[ri] = '0' if rev[ri] == '1' else '1'    # 스위치 토글
                
#         if rev not in visited:    # 변경된 적이 없는 상태일 때만,
#             q.append((rev, cnt + 1))    # 횟수 1 늘려서 q에 넣어주고,
#             visited.append(rev)    # 방문 처리
            
# print(ans)