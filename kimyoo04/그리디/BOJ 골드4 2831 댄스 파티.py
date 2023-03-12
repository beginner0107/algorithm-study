# https://www.acmicpc.net/problem/2831

"""
문제
남자 N명과 여자 N명이 상근이가 주최한 댄스 파티에 왔다. 상근이는 모든 사람의 키를 알고있다. 각 남자는 모두 여자와 춤을 출 수 있고, 여자는 남자와 춤을 출 수 있다. 모든 사람은 많아야 한 사람과 춤을 출 수 있다.

모든 남자는 자신이 선호하는 여자와 춤을 추려고 한다. 각 남자가 선호하는 여자는 두 가지 유형이 있는데, 한 유형은 자신보다 키가 큰 여자이고, 다른 유형은 자신보다 키가 작은 유형이다. 여자도 남자와 마찬가지로 자신이 선호하는 남자와 춤을 추려고 한다. 각 여자가 선호하는 남자도 남자와 비슷하게 두 유형이 있다. (자신보다 키가 큰 남자, 작은 남자) 키가 같은 남자와 여자가 춤을 추는 일은 일어나지 않는다.

이때, 상근이는 각 사람의 키와 선호하는 이성 유형을 알고 있다. 이런 조건을 가지고 춤을 출 쌍을 만들어 주려고 한다. 상근이는 최대 몇 쌍을 만들 수 있을까?

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄에는 남자의 키가 밀리미터 단위로 주어진다. 키는 절댓값이 1500보다 크거나 같고, 2500보다 작거나 같은 정수이다. 사람의 키는 주어지는 값의 절댓값이다. 키가 양수인 경우에는 자신보다 키가 큰 여자와 춤을 추기를 원하는 남자이고, 음수인 경우에는 키가 작은 사람과 춤을 추기를 원하는 남자이다.

셋째 줄에는 여자의 키가 밀리미터 단위로 주어진다. 키의 범위나 의미 역시 남자와 동일하다.

출력
첫째 줄에 상근이가 만들어 줄 수 있는 쌍의 최댓값을 출력한다.

예제 입력 1
1
-1800
1800

예제 출력 1
0

예제 입력 2
1
1700
-1800

예제 출력 2
1

예제 입력 3
2
-1800 -2200
1900 1700

예제 출력 3
2
"""

"""
핵심
- 남자 여자의 키의 합이 0이면 매칭 x, 음수이면 매칭, 양수이면 매칭 x
- 매칭되는 남자와 여자는 같이 양수이거나, 음수이면 매칭 x
- 가장 작은 사람이 가장 작은 사람을 만나기 -> 작은 사람끼리 먼저 매칭
"""

import sys; input=sys.stdin.readline

N = int(input())

males = map(int, input().split())
females = map(int, input().split())

# plus_male, minus_male, plus_female, minus_female
pm, mm, pf, mf = [], [], [], []

# + 와 - 구분 / 큰 키 순으로 정렬
for male in males:
    if male > 0:
        pm.append(male)
    else:
        mm.append(male)

for female in females:
    if female > 0:
        pf.append(female)
    else:
        mf.append(female)

pm.sort(); mm.sort(reverse=True)
pf.sort(); mf.sort(reverse=True)

def match(minus, plus):
    cnt = 0
    while minus:
        m = minus.pop()
        while plus :
            p = plus.pop()
            # 두 이성을 더했을 때 음수가 나오면
            if m + p < 0:
                cnt += 1 # 매칭
                break
    return cnt

print(match(mf, pm) + match(mm, pf))