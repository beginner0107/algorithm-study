# 힌트를 확인하니, 튜플 형태를 이용해야하는 것 같음
# 우선 입력을 튜플로 받고, 시작 시간을 기준으로 정렬해보자
# n: 회의의 수, session: 각 회의 시간을 튜플형태로 저장하는 리스트
# ss_max: 최대 회의 수, ss_time: 현재 시간

n = int(input())
session = []
ss_max, ss_time = 0, -1
for _ in range(n):
    session.append(tuple(map(int, input().split())))
    
session.sort(key=lambda s: [s[1], s[0]])    # 회의가 끝나는 시간, 시작 시간 순서대로 정렬
print(session)

# 회의가 끝나는 시간, 시작 시간이 더 먼저인 순서대로 회의실 배정
for s, t in session:
    if s >= ss_time:    # 회의 시작 시간이 지금보다 크거나 같으면
        ss_time = t    # 회의 끝나는 시간을 현재 시간에 저장
        ss_max += 1    # 회의수 더해주기
        
print(ss_max)