# https://school.programmers.co.kr/learn/courses/30/lessons/42883

"""
핵심
- k개 만큼 지운 후에 가장 큰 수 찾기
- 정렬은 불가능
- 다음 나오는 숫자가 이전에 나오는 숫자보다 작을 경우 k가 있는 경우에 계속 제거 (스텍 자료구조 사용)
"""

def solution(number, k):
    stack = [] # stack 자료구조 사용

    for n in number:
        # 이전 수가 작으면, k가 있으면 계속 빼내기
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1

        stack.append(n)

    # k 가 남았을 때 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)