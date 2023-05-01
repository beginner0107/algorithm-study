# https://school.programmers.co.kr/learn/courses/30/lessons/42885

"""
핵심
- 가장 가벼운 사람과 가장 큰 사람 2명을 한번에 실을수록 좋다
- 정렬을 해주는 것이 좋다.
"""

# 시간초과 한 방법
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    while people:
        answer += 1
        a = people.pop()
        for i in range(0, len(people)):
            if a + people[i] <= limit:
                a = people.pop(i)
                break

    return answer


# 정답 투포인터로 그리디 탐색
def solution1(people, limit):
    answer = 0
    people = sorted(people)

    # 왼쪽, 오른쪽 인덱스
    l = 0
    r = len(people)-1

    while l <= r:
        # limit 보다 클 때
        if people[l] + people[r] > limit:
            answer += 1
            r -= 1
        # limit 보다 작을 때
        else:
            answer += 1
            r -= 1
            l += 1

    return answer