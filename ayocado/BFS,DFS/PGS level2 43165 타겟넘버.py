"""
PGS 43165 타겟 넘버
● 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43165
    사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
    숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

● 입출력 예시
    numbers             target          return
    [1, 1, 1, 1, 1]     3               5
    [4, 1, 2, 1]        4               2

● 풀이 과정
1. 큐를 이용한 BFS
2. 큐에 [+숫자, 인덱스], [-숫자, 인덱스]를 push
3. popleft 후, [기존값+숫자, 다음 인덱스], [기존값-숫자, 다음 인덱스]를 push
4. 인덱스가 끝에 달했을 때, 숫자 == target 이면 answer += 1
"""

from collections import deque

def solution(numbers, target):
    queue = deque()
    answer = 0

    # 초기 노드
    queue.append([numbers[0], 0])       # [더할 경우, 인덱스]
    queue.append([-1 * numbers[0], 0])  # [뺄 경우, 인덱스]

    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        if idx != len(numbers):
            queue.append([tmp + numbers[idx], idx])  # 다음 인덱스에 대한 값을 더함
            queue.append([tmp - numbers[idx], idx])  # 다음 인덱스에 대한 값을 뺌
        else:
            if tmp == target:
                answer += 1
    return answer