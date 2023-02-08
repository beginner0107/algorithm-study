# https://www.acmicpc.net/problem/15649

"""
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

"""
핵심
- 순서를 고려하여 수를 1열로 세우는 방식 (Permutation, 순열)

"""


import sys; input=sys.stdin.readline

# 함수 호출 스택 구현 방법
def back(n_list):
    if len(n_list) == M: # 배열의 길이 M
        print(" ".join(map(str, n_list)))
        return

    for i in range(1, N+1): # 1 ~ N
        if i in n_list:
            continue
        back(n_list + [i])

    """
    # stack 동작 구현 방법

    for i in range(1, n + 1):
        if i in s:
        continue
        s.append(i)
        f()
        s.pop()
    """



# N 사용할 숫자 수
# M 배열의 길이
N, M = map(int, input().split())

back([])


"""
[다른 사례]
- 순열을 그대로 활용
from itertools import permutations

n, m = map(int, input().split())
p = permutations(range(1, n+1), m)

for i in p:
    print(" ".join(map(str, i)))
"""
