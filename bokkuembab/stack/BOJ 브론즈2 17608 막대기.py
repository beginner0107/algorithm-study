import sys
input = sys.stdin.readline

n = int(input())    # 막대기의 개수
visible = []    # 보이는 막대기의 길이
sticks = []         # 막대기의 길이 및 순서 저장
for _ in range(n):
    sticks.append(int(input()))

visible.append(sticks[-1])
m = sticks.index(max(sticks[::-1]))
for s in range(n-2, m - 1, -1):
    
    if visible[-1] < sticks[s]:     # 막대기가 새로 들어올 때마다 기존에 있는 막대기와 길이 비교
        visible.append(sticks[s])       # 현재 보이는 막대기보다 길이가 길면, 새로운 막대기 추가

print(len(visible))