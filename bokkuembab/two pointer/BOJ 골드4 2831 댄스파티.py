# 자신이 선호하는 남자와 춤을 추려고 함
# 1. 자신보다 키가 큼, 2. 자신보다 키가 작음
# 키가 같은 남자와 여자가 춤을 추는 일은 일어나지 않음
# 춤을 출 쌍을 최대 몇 쌍 만들 수 있을까?

# abs 기준으로 정렬해야 할까...?
# ++끼리, --끼리 춤 출 수 X, -+ 또는 +-끼리 춤 출 수 O
# 리스트를 남녀 음수, 양수끼리 나눠야 하나

import sys
input = sys.stdin.readline

n = int(input())    # 여자, 남자의 수
# 키가 양수: 자신보다 키가 큰 사람과 춤을 추기를 원함, 음수: 키가 작은 사람과 춤을 추기를 원함
men = list(map(int, input().split()))    # 남자의 키 리스트
women = list(map(int, input().split()))    # 여자의 키 리스트

# 춤을 출 쌍
couple = 0

# 남녀 각각 음수, 양수 리스트로 나누기
men_p, men_m = [], []
for m in men:
    if m < 0:
        men_m.append(abs(m))
    else:
        men_p.append(m)
        
women_p, women_m = [], []
for w in women:
    if w < 0:
        women_m.append(abs(w))
    else:
        women_p.append(w)

# 절대값 순서대로 정렬하기
men_m.sort()
men_p.sort()
women_m.sort()
women_p.sort()

# print(men_m, men_p, women_m, women_p)

# 남 +, 여 - 엮어주기
left, right = 0, 0
while left < len(men_p) and right < len(women_m):

    if (men_p[left] < women_m[right]):    # 여자가 남자보다 크다면, 커플 성사
        couple += 1    # 커플 1 늘려주고,
        left += 1    # 남, 녀 둘 다 하나씩 추가
        right += 1
    else:    # 여자가 남자보다 작거나 같다면, 커플 결렬 -> 여자를 키워줘야 함
        right += 1
        
# 남 -, 여 + 엮어주기
left, right = 0, 0
while left < len(men_m) and right < len(women_p):

    if (men_m[left] > women_p[right]):    # 남자가 여자보다 크다면, 커플 성사
        couple += 1    # 커플 1 늘려주고,
        left += 1    # 남, 녀 둘 다 하나씩 추가
        right += 1
    else:    # 남자가 여자보다 작거나 같다면, 커플 결렬 -> 남자를 키워줘야 함
        left += 1

print(couple)


# 3
# 2000 -1800 -2200
# 1900 1700 -2000

# -1800 2000 -2200 -2400
# -1600 1700 1900 -2000

# 남-: -1800 -2200 -2400
# 남+: 2000
# 여-: -1600 -2000
# 여+: 1700 1900