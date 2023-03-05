import sys
from collections import deque

N = int(sys.stdin.readline())
man = list(map(int, sys.stdin.readline().split()))
women = list(map(int, sys.stdin.readline().split()))
"""
작은 여자랑 춤추고 싶은 남자, 큰 남자랑 춤추고 싶은 여자
남자는 내림차순 정렬, 여자는 오름차순 정렬
여자 첫번째부터 남자 대입해보기 > 매칭안되면 남자 deque > 매칭되면 deque, count + 1, 다음 여자로
> 모든 여자 대입해보거나, 모든 남자 deque되면 완료
"""
man_minus = deque(sorted([i for i in man if i < 0], reverse=True))
women_minus = deque(sorted([i for i in women if i < 0], reverse=True))
man_plus = sorted([i for i in man if i > 0])
women_plus = sorted([i for i in women if i > 0])
count = 0
flag = 0
for height_women in women_plus:
    height_man = 0
    while height_man <= height_women:
        if len(man_minus) == 0:
            flag = 1
            break
        height_man = abs(man_minus.popleft())
    if flag != 1:
        count += 1
"""
큰 여자랑 춤추고 싶은 남자, 작은 남자랑 춤추고 싶은 여자
남자 오름차순 정렬, 여자 내림차순 정렬
첫번째 남자부터 여자 매칭 > 매칭 안되면 여자 deque > 매칭되면 여자 deque, count + 1, 다음 남자
> 모든 남자 매칭해보거나, 모든 여자 deque 되면 완료
"""
flag = 0
for height_man in man_plus:
    height_women = 0
    while height_women <= height_man:
        if len(women_minus) == 0:
            flag = 1
            break
        height_women = abs(women_minus.popleft())
    if flag != 1:
        count += 1

print(count)